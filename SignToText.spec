# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['SignToText.py'],
             pathex=[],
             binaries=[],
             datas=[('C:\\Users\\Sahista\\PycharmProjects\\Lingua_Virtual\\venv\\Lib\\site-packages\\hunspell', 'hunspell'),
             ('C:\\Users\\Sahista\\PycharmProjects\\Lingua_Virtual\\venv\\Lib\\site-packages\\cacheman', 'cacheman'),
             ('C:\\Users\\Sahista\\PycharmProjects\\Lingua_Virtual\\venv\\Lib\\site-packages\\past', 'past'),
             ('C:\\Users\\Sahista\\PycharmProjects\\Lingua_Virtual\\venv\\Lib\\site-packages\\future', 'future'),
             ('C:\\Users\\Sahista\\PycharmProjects\\Lingua_Virtual\\venv\\Lib\\site-packages\\keras', 'keras')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='SignToText',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='SignToText')
