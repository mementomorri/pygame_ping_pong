# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['__init__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['ping_pong/conf.py', 'ping_pong/conf.py', 'ping_pong/encode_imgs.py', 'ping_pong/game_sprite.py', 'ping_pong/images_b64.py', 'ping_pong/racket.py', 'ping_pong/type_hints.py', 'ping_pong/window_interface.py'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ping-pong',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
