# -*- mode: python -*-

block_cipher = None

added_files = [
	('C:\\Users\\90499\\ServerCheck\\serverLog.txt', '.'),
	('C:\\Users\\90499\\ServerCheck\\requesthtml_Config.ini', '.')
	]

a = Analysis(['C:\\Users\\90499\\ServerCheck\\requesthtml.py'],
             pathex=['C:\\Users\\90499\\ServerCheck'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='requesthtml',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
