; Inno Setup Script for AIGIT Installer
[Setup]
AppName=AIGIT
AppVersion=1.0.0
DefaultDirName={pf}\AIGIT
DefaultGroupName=AIGIT
OutputDir=dist
OutputBaseFilename=AIGIT_Installer
SetupIconFile=installer\icon.ico
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\aigit.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"
Source: "config\*"; DestDir: "{app}\config"; Flags: recursesubdirs
Source: "error_logs\*"; DestDir: "{app}\error_logs"; Flags: recursesubdirs
Source: "docs\*"; DestDir: "{app}\docs"; Flags: recursesubdirs

[Icons]
Name: "{group}\AIGIT"; Filename: "{app}\aigit.exe"
Name: "{group}\Uninstall AIGIT"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\aigit.exe"; Description: "Run AIGIT"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
