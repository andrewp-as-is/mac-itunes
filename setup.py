import setuptools

setuptools.setup(
    name='mac-itunes',
    version='2020.12.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/.itunes-mute.applescript','scripts/.itunes-muted.applescript','scripts/.itunes-next.applescript','scripts/.itunes-pause.applescript','scripts/.itunes-play-playlist.applescript','scripts/.itunes-play-track.applescript','scripts/.itunes-play.applescript','scripts/.itunes-playlists.applescript','scripts/.itunes-prev.applescript','scripts/.itunes-state.applescript','scripts/.itunes-stop.applescript','scripts/.itunes-unmute.applescript','scripts/.itunes-volume.applescript','scripts/itunes','scripts/itunes-frontmost','scripts/itunes-kill','scripts/itunes-mute','scripts/itunes-muted','scripts/itunes-next','scripts/itunes-pause','scripts/itunes-pid','scripts/itunes-play','scripts/itunes-play-track','scripts/itunes-playlists','scripts/itunes-prev','scripts/itunes-state','scripts/itunes-stop','scripts/itunes-unmute','scripts/itunes-volume']
)
