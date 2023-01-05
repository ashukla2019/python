# -*- coding: utf-8 -*-
__author__ = 'z0039vxr'
__copyright__ = "Copyright 2017-2018, Siemens RA"
__credits__ = ["Julian Martinez"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Julian Martinez"
__email__ = "julian.martinez@siemens.com"
# 'status' could be 'Prototype', 'Development' or 'Production'
__status__ = "Development"
__docformat__ = "restructuredtext"
"""
Module to download baseline from Synergy.
:author: Julian Martinez
:version: 0.1
:status: Production
:change: v0.1 Creation
"""

# ########################################
# ## Imports #############################
# ########################################
import ConfigParser
import fnmatch
import os
import tqdm
import re
import shutil
import stat
import subprocess
import sys
import time
import traceback

# ########################################
# ## Global Variables: definition ########
# ########################################

# Contains the status message to display at the end of the run
summaryStatusFileHandle = 0

# From INI file
pathBuildHost = ""
pathHostEnvironment = ""
pathExeHost = ""
pathCodeInstr = ""
unitToMapCode = ""
pathSources = ""
baselineName = ""
pathCode = ""
processBaseline = ""
userSynergy = ""
pwdSynergy = ""
listOfAllFiles = []
listOfFiles = []
listOfPaths = []
scriptLocation = os.getcwd()
DOWNLOAD_INI_FILE = 'download.ini'
SY_EXE_FILE = 'ccm.exe'

# Install directories
# Synergy. If path is updated, get Synergy install directory from path. If not, let it empty and get it from ini file.
pathVariableEnviron = os.environ['PATH'].split(";")
if len([s for s in pathVariableEnviron if "Synergy" in s]) != 0:
    syInstallDir = [s for s in pathVariableEnviron if "Synergy" in s][0]
else:
    syInstallDir = ""


# ########################################
# ## Auxiliary procedures ################
# ########################################


def addToSummaryStatus(message):
    """
    This is just a wrapper so that we can capture the main status messages for
    display at the end of the process
    :param message: string to be printed
    :return: summary updated
    """
    global summaryStatusFileHandle

    print message
    summaryStatusFileHandle.write(message + '\n')
    summaryStatusFileHandle.flush()


def sectionBreak(message):
    """
    Insert a break in the summary status.
    :param message: string to be printed
    :return: summary updated
    """
    print '\n\n'
    print '---------------------------------------------------------------------------------------------'
    print '---------------------------------------------------------------------------------------------'
    if len(message) > 0:
        print message
        print '---------------------------------------------------------------------------------------------'
        print '---------------------------------------------------------------------------------------------'


def getTimeString(milliSeconds):
    """
    Convert a milliseconds float value to a seconds string
    :param milliSeconds: time value in milliseconds to be converted
    :return: string in minutes or seconds
    """
    seconds = milliSeconds / 1000
    if seconds > 60:
        return "%1.1f " % (seconds / 60) + ' minutes'
    else:
        return "%1.1f " % seconds + ' seconds'


def fatalError(errorString, causeError):
    """
    Print an error string and raise an exception.
    :param errorString: string to be printed
    :param causeError: string to detect the application that causes the error
    :return: an exception
    """
    print errorString
    print ('Terminating ...\n\n')
    raise Exception('Termination Error. Unknown Origin')


def runCommand(command, abortOnError=False, verboseOutput=False):
    """
    Run Command with subprocess.Popen and return status
    If the fatal flag is true, we abort the process, if
    not, we print the stdout and continue ...
    :param command: string with the command to be run
    :param abortOnError: boolean to abort on error
    :param verboseOutput: controls the output of the stdout from all commands
    :return: the cmd output and the exit code
    """

    cmdOutput = ''

    if verboseOutput:
        print '   running command: ' + command
    vcProc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,
                              shell=True)
    stdoutLines = iter(vcProc.stdout.readline, "")
    stderrLines = iter(vcProc.stderr.readline, "")

    for line in stdoutLines:
        if verboseOutput:
            sys.stdout.write(line)
        # else:
        #     sys.stdout.write('.')
        cmdOutput += line

    for line in stderrLines:
        if verboseOutput:
            sys.stderr.write(line)
        # else:
        #     sys.stderr.write('.')
        cmdOutput += line

    vcProc.stdout.close()
    exitCode = vcProc.wait()
    if verboseOutput:
        sys.stdout.write('\n')

    # handle all errors ...
    if exitCode != 0:
        # In all cases, we print out the
        print '   command returned a non-zero exit code: ' + str(exitCode)
        print '   stdout/stderr => '
        print cmdOutput
        if abortOnError:
            raise Exception('Command failed')

    return cmdOutput, exitCode


def readINIFile():
    """
    This function will look for optionName in the local directory
    coverage.ini file and return the value.  If the option is not
    found or there is not a CCAST_.CFG file we return ""
    :param
    :return: update global path variables
    """

    global processBaseline
    global baselineName
    global pathSources
    global pathHostEnvironment
    global userSynergy
    global pwdSynergy
    global unitToMapCode
    global syInstallDir
    global pathBuildHost
    global pathCode
    global pathExeHost
    global pathCodeInstr

    sectionBreak('')
    addToSummaryStatus('Reading INI file...')
    startMS = time.time() * 1000.0

    try:
        iniFile = os.path.join(scriptLocation, DOWNLOAD_INI_FILE)
        # if there is a local file, and it is the one we want then read file and update variables
        if os.path.isfile(DOWNLOAD_INI_FILE) and (os.stat(iniFile) == os.stat(DOWNLOAD_INI_FILE)):
            configFile = ConfigParser.ConfigParser()
            configFile.readfp(open(iniFile))
            processBaseline = configFile.get('General', 'downloadbaseline')  # tipically 'TRUE/FALSE'

            baselineName = configFile.get('DownloadBaseline', 'baseline')

            pathAux = configFile.get('Paths', 'pathsources')  # tipically 'D:\WorkingDir\CODE_COVERAGE\SOURCES'
            pathSources = os.path.join(pathAux, baselineName)
            pathHostEnvironment = os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT')

            userSynergy = configFile.get('DownloadBaseline', 'user')
            pwdSynergy = configFile.get('DownloadBaseline', 'password')

            unitToMapCode = configFile.get('VectorCast', 'unittomapcodehost')  # tipically 'Q:'

            # If install directory can not be read from path environment, read it from INI file
            if syInstallDir == "":
                # tipically 'C:\IBM\Rational\Synergy\7.2.1\bin\'
                pathAux = configFile.get('DownloadBaseline', 'pathsynergy')
                syInstallDir = os.path.join(pathAux, SY_EXE_FILE)

            pathBuildHost = os.path.join(pathSources, 'RBC_MPM_CODE', 'BUILD_HOST')
            pathCode = os.path.join(pathSources, 'RBC_MPM_CODE', 'CODE', 'APPL')
            pathExeHost = os.path.join(pathSources, 'RBC_MPM_CODE', 'EXE_HOST')
            pathCodeInstr = os.path.join(pathSources, 'RBC_MPM_CODE', 'CODE', 'APPL', 'CODE_INSTR')

        endMS = time.time() * 1000.0
        addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')
    except:
        addToSummaryStatus('   error reading coverage INI file...')
        raise ValueError('Error reading coverage INI file.')


def generateLists():
    """
    Generate list of files, list of filtered files and list of paths
    :return:
    """
    global listOfFiles
    global listOfAllFiles
    global listOfPaths
    global pathCode

    sectionBreak('')
    addToSummaryStatus('Generate lists...')
    startMS = time.time() * 1000.0

    # Preprocess for tqdm
    dirCount = 0
    fileCount = 0
    for root, dirs, files in os.walk(pathCode):
        dirCount += len(dirs)
        fileCount += len(files)
    addToSummaryStatus('   found ' + str(fileCount) + ' total source files')
    addToSummaryStatus('   found ' + str(dirCount) + ' total subdirs')

    # Create listOfAllFiles
    addToSummaryStatus('   creating list of all files')
    for root, dirs, files in tqdm.tqdm(os.walk(pathCode), ascii=True, total=fileCount, desc="listOfAllFiles"):
        for file in files:
            absFile = os.path.join(root, file)
            listOfAllFiles.append(absFile)

    # Create listOfPaths
    addToSummaryStatus('   creating list of paths')
    excludeDirs = r'TYPES|CONSTANTS|ERROR_CODES|\\PACKET_TO_ERTMS_MANAGER_L2\\'
    pExcludeDirs = re.compile(excludeDirs, re.IGNORECASE)
    for root, dirs, files in tqdm.tqdm(os.walk(pathCode), ascii=True, total=dirCount, desc="listOfPaths"):
        if not dirs and re.search(pExcludeDirs, root) is None:
            listOfPaths.append(root)

    # Create listOfFiles
    addToSummaryStatus('   creating list of filtered files')
    listOfFiles = []
    listOfFiles = listOfAllFiles[:]
    for file in tqdm.tqdm(listOfAllFiles, ascii=True, total=fileCount, desc="listOfFiles"):
        # Get the file name and the extension
        fileName, fileExtension = os.path.splitext(file)
        # Filtering files
        if fileExtension == '.adb' or fileExtension == '.bdy':
            # If file extension is 'adb' it must be deleted, except 'state_transition_table' or 'stt'
            filePartNameA = 'state_transition_table'
            filePartNameB = 'stt'
            if filePartNameA not in fileName and filePartNameB not in fileName:
                # pdb.set_trace()
                # Delete the file from the list
                listOfFiles.remove(file)
        elif fileExtension == '.ads' or fileExtension == '.spc':
            listOfFiles.remove(file)
            """
            # If the same file with extension ads exists, delete it
            absfile = fileName + '.ads'
            if os.path.exists(absfile):
                # Delete the file from the list
                listOfFiles.remove(file)
            """
        elif fileExtension == '.sep':
            # If the same file with extension ada or asp exist, delete it
            absfile = fileName + '.ada'
            if os.path.exists(absfile):
                # Delete the file from the list
                listOfFiles.remove(file)
            absfile = fileName + '.asp'
            if os.path.exists(absfile):
                # Delete the file from the list
                listOfFiles.remove(file)
        elif fileExtension == '.ada':
            # If file is 'test_point_s', delete it
            filePartNameA = 'test_point_s'
            if filePartNameA in fileName:
                # Delete the file from the list
                listOfFiles.remove(file)
        else:
            # Delete the file from the list
            listOfFiles.remove(file)
    addToSummaryStatus('   found ' + str(len(listOfFiles)) + ' filtered source files')

    endMS = time.time() * 1000.0
    addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')


def downloadBaseline():
    """
    Download the baseline defined in the INI file.
    :return:
    """
    global syInstallDir
    global pathSources
    global baselineName
    global pathBuildHost
    global pathCode
    global pathExeHost
    global pathCodeInstr
    global processBaseline

    sectionBreak('')
    addToSummaryStatus('Downloading baseline...')
    startMS = time.time() * 1000.0

    try:
        if processBaseline == 'TRUE':

            # Command strings
            ccmStopQuery = syInstallDir + '\ccm stop'
            ccmStartQuery = syInstallDir + '\ccm start -s https://esplx325:8400 -d /datos/ccmdb/CoE_ERTMS -n ' + \
                            userSynergy + ' -pw ' + pwdSynergy
            ccmCopyToFileSystem = syInstallDir + '\ccm copy_to_file_system -path ' + pathSources + \
                                  ' -recurse RBC_MPM_CODE:' + baselineName

            addToSummaryStatus('   closing previous SYNERGY session...')
            stdOut, exitCode = runCommand(ccmStopQuery, False, True)

            addToSummaryStatus('   opening SYNERGY session...')
            stdOut, exitCode = runCommand(ccmStartQuery, False, True)

            addToSummaryStatus('   downloading baseline...')
            stdOut, exitCode = runCommand(ccmCopyToFileSystem, False, True)

            addToSummaryStatus('   closing SYNERGY session...')
            stdOut, exitCode = runCommand(ccmStopQuery, False, True)

            # It is not needed to check the paths because the code is downloaded with this structure
        else:
            # Paths must be checked in order to test if script can be executed
            # Check if BUILD_HOST exist
            # If paths needed exist, nothing to do
            if os.path.isdir(pathBuildHost) and os.path.isdir(pathCode) and os.path.isdir(pathExeHost):
                addToSummaryStatus('   paths in SOURCES OK...')
            else:
                # return an error
                raise ValueError('Any of the paths needed do not exist.')

        # Create directory for code instrumentalized
        if os.path.exists(pathCodeInstr):
            shutil.rmtree(pathCodeInstr, ignore_errors=True)
        os.mkdir(pathCodeInstr)
        addToSummaryStatus('   path for code instrumentalized created...')

        # Generate list of files and paths
        generateLists()
        addToSummaryStatus('   list of files and paths created...')

        endMS = time.time() * 1000.0
        addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')

    except Exception, err:
        # If no session is open, we continue
        if str(err) == 'Warning: No sessions found':
            addToSummaryStatus('   no sessions found, run \'ccm start\' to start a session, continuing...')
        elif str(err) == 'Any of the paths needed do not exist.':
            addToSummaryStatus('   any of the paths needed do not exist...')
            raise
        else:
            raise


def deletePrevEnvironment():
    """
    This function delete the previous compilation environment, if it exists.
    :return:
    """

    global pathSources

    sectionBreak('')
    addToSummaryStatus('Deleting environment  ...')
    startMS = time.time() * 1000.0

    if os.path.exists(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB')):
        for root, dirs, files in os.walk(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB')):
            for filename in files:
                fullPath = os.path.join(root, filename)
                os.chmod(fullPath, stat.S_IWRITE)
                os.remove(fullPath)

    endMS = time.time() * 1000.0
    addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')


def buildCompilationEnvironment():
    """
    This function will build a new compilation environment, in order to create a unique library (for VectorCAST Ada) and
    take into account the instrumentalized code in a different folder.
    :return:
    """

    global pathCodeInstr
    global pathBuildHost
    global pathHostEnvironment
    global unitToMapCode

    listOfFuentesFiles = []
    listOfBatFiles = []

    sectionBreak('')
    addToSummaryStatus('Building Compilation Environment ...')
    startMS = time.time() * 1000.0

    # 01. Update 'fuentes.txt' with the new path for the instrumentalized code
    # List all files in \CODE_INSTR
    addToSummaryStatus('   listing instrumentalized code ...')
    listOfFuentesFiles = [f for f in os.listdir(pathCodeInstr) if os.path.isfile(os.path.join(pathCodeInstr, f))]

    # 02. Search the file name into all 'fuentes.txt' and make a copy of the file into "fuentes_mod.txt"
    addToSummaryStatus('   searching in fuentes.txt ...')
    numberFuentesFiles = 0
    for root, dirnames, filenames in os.walk(pathBuildHost):
        for filename in fnmatch.filter(filenames, '*.txt'):
            numberFuentesFiles += 1
    for root, dirs, files in tqdm.tqdm(os.walk(pathBuildHost), ascii=True, total=numberFuentesFiles,
                                       desc="fuentes_mod"):
        for file in files:
            if file == "fuentes.txt":
                with open(os.path.join(root, file)) as inputFuente, \
                        open(os.path.join(root, "fuentes_mod.txt"), "wb") as outputFuente:
                    for line in inputFuente:
                        path, filename = os.path.split(line)
                        if line != "\n":
                            if any(filename[:-1].lower() in s for s in listOfFuentesFiles):
                                outputFuente.write(line.replace(path, "R:\CODE_INSTR"))
                            else:
                                outputFuente.write(line)

    endMS = time.time() * 1000.0
    addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')

    # 03. Modify .bat files
    addToSummaryStatus('   modifying bat files ...')
    startMS = time.time() * 1000.0
    # list *.bat files
    for root, dirs, files in os.walk(pathBuildHost):
        for file in files:
            fileName, fileExt = os.path.splitext(file)
            if fileExt == '.bat':
                listOfBatFiles.append(os.path.join(root, file))
    # create *_mod.bat files and modify them
    for file in tqdm.tqdm(listOfBatFiles, ascii=True, total=len(listOfBatFiles), desc="bat_mod"):
        fullFileName = os.path.basename(file)
        fileName, fileExt = os.path.splitext(fullFileName)
        # create 'mod' bat files
        modFile = os.path.join(os.path.dirname(file), fileName + '_mod' + fileExt)
        shutil.copyfile(file, modFile)
        # modify 'mod' bat files
        if fileName == 'mensajes':
            with open(file) as inputFile, open(modFile, 'wb') as outputFile:
                for line in inputFile:
                    if "set /p intro=" in line:
                        # This sentence in the batch file waits for an ENTER keystroke. This is not needed, so skip the
                        # line.
                        continue
                    else:
                        # nothing to do
                        outputFile.write(line)
        if fileName == 'build':
            with open(file) as inputFile, open(modFile, 'wb') as outputFile:
                for line in inputFile:
                    outputFile.write(line.replace('.bat', '_mod.bat'))
        if fileName == 'install':
            with open(file) as inputFile, open(modFile, 'wb') as outputFile:
                for line in inputFile:
                    if "set DRIVE_LIB" in line:
                        outputFile.write("set DRIVE_LIB=" + unitToMapCode + "\n")
                    elif "ADA_95" in line:
                        outputFile.write("set DIR_LIB=" + pathHostEnvironment + "\LIB\n")
                    elif ".bat" in line:
                        outputFile.write(line.replace('.bat', '_mod.bat'))
                    elif "DIR_LIB_" in line:
                        # there will be only one LIB, so these lines will be skipped
                        continue
                    else:
                        # nothing to do
                        outputFile.write(line)
        if fileName == 'create_libs':
            with open(file) as inputFile, open(modFile, 'wb') as outputFile:
                for line in inputFile:
                    if ":::" in line:
                        outputFile.write("if not exist %DIR_LIB% md %DIR_LIB%\n")
                        outputFile.write("cd %DIR_LIB%\n")
                        outputFile.write("adaopts -pi end %DIR_DLL%\n")
                        outputFile.write("adaopts -pi end \"%DIR_ADA%\lib\\rts\"\n")
                        outputFile.write("adaopts -pi end \"%DIR_ADA%\win32ada\\binding\lib\"\n")
                        outputFile.write("adaopts -pi end \"%DIR_ADA%\winapi\\v4.1\\binding\\ascii\lib\"\n")
                        break
                    else:
                        # nothing to do
                        outputFile.write(line)
        if fileName == 'linkado':
            with open(file) as inputFile, open(modFile, 'wb') as outputFile:
                for line in inputFile:
                    outputFile.write(line.replace('DIR_LIB_MAIN', 'DIR_LIB'))
        if "comp_" in fileName:
            with open(file) as inputFile, open(modFile, 'wb') as outputFile:
                for line in inputFile:
                    if "fuentes.txt" in line:
                        line = line.replace("fuentes.txt", "fuentes_mod.txt")
                    if "%DIR_LIB_" in line:
                        line = line.replace("%DIR_LIB" + line.split("%DIR_LIB")[1].split("%")[0] + "%", "%DIR_LIB%")
                    outputFile.write(line)

    endMS = time.time() * 1000.0
    addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')


def mapUnits():
    """
    This funtion maps the units needed for the process. It is like 'mapear.bat'
    :return:
    """

    global pathSources
    global pathBuildHost

    sectionBreak('')
    addToSummaryStatus('Mapping units  ...')
    startMS = time.time() * 1000.0

    try:
        substStr = 'C:\Windows\System32\subst R: /D'
        stdOut, exitCode = runCommand(substStr, False, True)
    except:
        pass
    try:
        substStr = 'C:\Windows\System32\subst R: ' + os.path.join(pathSources, 'RBC_MPM_CODE\CODE\APPL')
        stdOut, exitCode = runCommand(substStr, False, True)
    except:
        addToSummaryStatus('   ERROR mapping ' + os.path.join(pathSources, 'RBC_MPM_CODE\CODE\APPL') + ' in R:  ...')
        pass
    try:
        substStr = 'C:\Windows\System32\subst S: /D'
        subprocess.check_output(substStr)
    except:
        pass
    try:
        substStr = 'C:\Windows\System32\subst S: ' + os.path.join(pathSources, 'RBC_MPM_CODE\CODE\PLATFORM_HOST')
        stdOut, exitCode = runCommand(substStr, False, True)
    except:
        addToSummaryStatus('   ERROR mapping ' + os.path.join(pathSources, 'RBC_MPM_CODE\CODE\PLATFORM_HOST') +
                           ' in S:  ...')
        pass
    try:
        substStr = 'C:\Windows\System32\subst K: /D'
        stdOut, exitCode = runCommand(substStr, False, True)
    except:
        pass
    try:
        substStr = 'C:\Windows\System32\subst K: ' + os.path.join(pathSources, 'RBC_MPM_CODE\CODE\LOAD_DATA_BANK')
        stdOut, exitCode = runCommand(substStr, False, True)
    except:
        addToSummaryStatus('   ERROR mapping ' + os.path.join(pathSources, 'RBC_MPM_CODE\CODE\LOAD_DATA_BANK') +
                           ' in K:  ...')
        pass
    try:
        substStr = 'C:\Windows\System32\subst M: /D'
        stdOut, exitCode = runCommand(substStr, False, True)
    except:
        pass
    try:
        substStr = 'C:\Windows\System32\subst M: ' + pathBuildHost
        stdOut, exitCode = runCommand(substStr, False, True)
    except:
        addToSummaryStatus('   ERROR mapping ' + pathBuildHost + ' in M:  ...')
        pass

    endMS = time.time() * 1000.0
    addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')


def copyLibraries():
    """
    This function copies the libraries needed to compile the code.
    :return:
    """

    global pathSources

    sectionBreak('')
    addToSummaryStatus('Copying libraries  ...')
    startMS = time.time() * 1000.0

    if os.path.exists(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\DLL')):
        shutil.rmtree(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\DLL'), ignore_errors=True)
    if os.path.exists(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\main')):
        shutil.rmtree(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\main'), ignore_errors=True)
    os.makedirs(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\DLL'))
    os.makedirs(os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\main'))
    AleLibPath = 'F:\RBC_Storehouse\Formal\Versions\RBC_DLLs\LAST\ALE.lib'
    DesLibPath = 'F:\RBC_Storehouse\Formal\Versions\RBC_DLLs\LAST\des.lib'
    AleDllPath = 'F:\RBC_Storehouse\Formal\Versions\RBC_DLLs\LAST\ALE.dll'
    DesDllPath = 'F:\RBC_Storehouse\Formal\Versions\RBC_DLLs\LAST\des.dll'
    try:
        shutil.copy2(AleLibPath, os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\DLL'))
        addToSummaryStatus('   Copying ALE.lib  ...')
    except:
        addToSummaryStatus('   ERROR copying ALE.lib  ...')
        sys.exit("Error copying ALE.lib")
    try:
        shutil.copy2(DesLibPath, os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\DLL'))
        addToSummaryStatus('   Copying des.lib  ...')
    except:
        addToSummaryStatus('   ERROR copying des.lib  ...')
        sys.exit("Error copying des.lib")
    try:
        shutil.copy2(AleDllPath, os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\main'))
        addToSummaryStatus('   Copying ALE.dll  ...')
    except:
        addToSummaryStatus('   ERROR copying ALE.dll  ...')
        sys.exit("Error copying ALE.dll")
    try:
        shutil.copy2(DesDllPath, os.path.join(pathSources, 'RBC_MPM_HOST_ENVIRONMENT\LIB\main'))
        addToSummaryStatus('   Copying des.dll  ...')
    except:
        addToSummaryStatus('   ERROR copying des.dll  ...')
        sys.exit("Error copying des.dll")

    endMS = time.time() * 1000.0
    addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')


def executeCompilation():
    """
    This function will compile code. The process is:
       - execute install_mod.bat
    :return:
    """

    global pathBuildHost
    global pathHostEnvironment
    global pathExeHost

    sectionBreak('')
    addToSummaryStatus('Compiling  ...')
    startMS = time.time() * 1000.0

    stdOut, exitCode = runCommand(pathBuildHost + "\\install_mod.bat", False, True)

    # Copy the executable if it has been generated
    addToSummaryStatus('   copying executable to EXE_HOST...')
    try:
        shutil.copy(os.path.join(pathHostEnvironment, 'LIB', 'pc_rbc_main_s.exe'), pathExeHost)
        shutil.copy(os.path.join(pathHostEnvironment, 'LIB', 'pc_rbc_main_s.pdb'), pathExeHost)
    except:
        addToSummaryStatus('   error while copying the executable. Check LOG file...')

    endMS = time.time() * 1000.0
    addToSummaryStatus('   complete (' + getTimeString(endMS - startMS) + ')')


def main():
    """
    This module will download a baseline from Synergy.
    :return:
    """

    global summaryStatusFileHandle

    statusFile = 'downloadBL.log'
    summaryStatusFileHandle = open(statusFile, 'w', 1)

    addToSummaryStatus('Starting process ...')
    startMS = time.time() * 1000.0

    # 01. Read the config file.
    readINIFile()

    # 02. Download the baseline
    downloadBaseline()

    # 03. Delete previous environment, if it exists
    deletePrevEnvironment()

    # 04. Building compilation environment
    buildCompilationEnvironment()

    # 05. Mapping units
    mapUnits()

    # 06. Copy libraries
    copyLibraries()

    # 07. Compile code
    #executeCompilation()

    endMS = time.time() * 1000.0
    addToSummaryStatus('complete (' + getTimeString(endMS - startMS) + ')')

    summaryStatusFileHandle.close()


if __name__ == "__main__":
    try:
        main()
    except Exception, err:
        if str(err) != 'Download Baseline Error':
            print Exception, err
            print traceback.format_exc()
