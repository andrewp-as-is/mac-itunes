<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/badge/language-AppleScript-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-itunes.svg?maxAge=3600)](https://pypi.org/project/mac-itunes/)
[![](https://img.shields.io/npm/v/mac-itunes.svg?maxAge=3600)](https://www.npmjs.com/package/mac-itunes)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-itunes.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-itunes/)

#### Installation
```bash
$ [sudo] npm i -g mac-itunes
```
```bash
$ [sudo] pip install mac-itunes
```

#### Scripts usage
command|`usage`
-|-
`itunes` |`usage: itunes command [args]`
[`itunes-frontmost`](# "print 1 if 'iTunes.app' is frontmost, else 0") |`usage: itunes-frontmost`
`itunes-kill` |`usage: itunes-kill`
`itunes-mute` |`usage: itunes-mute`
`itunes-muted` |`usage: itunes-muted`
`itunes-next` |`usage: itunes-next`
`itunes-pause` |`usage: itunes-pause`
`itunes-pid` |`usage: itunes-pid`
`itunes-play` |`usage: itunes-play`
`itunes-play-track` |`usage: itunes-play-track track playlist`
`itunes-playlists` |`usage: itunes-playlists`
`itunes-prev` |`usage: itunes-prev`
`itunes-state` |`usage: itunes-state`
`itunes-stop` |`usage: itunes-stop`
`itunes-unmute` |`usage: itunes-unmute`
`itunes-volume` |`usage: itunes-volume [volume]`

#### Examples
```bash
$ itunes play
$ itunes pause
$ itunes stop
$ itunes next
$ itunes previous
```

volume
```bash
$ itunes volume 50
$ itunes volume
50
```

mute
```bash
$ itunes mute
$ itunes muted
1
$ itunes unmute
```

frontmost (`1` or `0`)
```bash
$ itunes frontmost
0
```

`iTunes.app` process
```bash
$ itunes pid
42
$ itunes kill
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>