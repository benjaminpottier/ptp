# ptp


**Exampple:**

```bash
ptp.py --top10
```
```
{"21 Bridges AKA Manhattan Lockdown": "210804"}
{"Jojo Rabbit": "210862"}
{"Midway": "210863"}
{"A Beautiful Day in the Neighborhood": "210861"}
{"Star Wars: Episode VII - The Force Awakens": "135930"}
{"Fahrenheit 9/11": "2886"}
{"The Coldest Game": "211135"}
{"Mestari Cheng": "211146"}
{"Mike Wallace Is Here": "206281"}
{"Bbaengban AKA Hit-and-Run Squad": "196692"}
```

```bash
ptp.py --list-torrents 210804
```
```
{"ReleaseName": "21.Bridges.2019.BDRip.x264-AAA", "Id": "748690"}
{"ReleaseName": "21.Bridges.2019.AMZN.WEB-DL.DDP2.0.H.264-NTG", "Id": "748254"}
{"ReleaseName": "21.Bridges.2019.720p.AMZN.WEB-DL.DDP5.1.H.264-NTG", "Id": "748255"}
{"ReleaseName": "21.Bridges.2019.720p.BluRay.DD5.1.x264-PbK", "Id": "749518"}
{"ReleaseName": "21.Bridges.2019.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTG", "Id": "748253"}
{"ReleaseName": "21.Bridges.2019.1080p.BluRay.x264-AAA", "Id": "748694"}
{"ReleaseName": "21.Bridges.2019.1080p.BluRay.DD5.1.x264-PbK", "Id": "749521"}
{"ReleaseName": "21.Bridges.2019.2160p.WEB-DL.DDP5.1.HEVC-BLUTONiUM", "Id": "749373"}
```

```bash
ptp.py --download "21.Bridges.2019.2160p.WEB-DL.DDP5.1.HEVC-BLUTONiUM" 749373
```

Downloads the .torrent file into your watch directory, the `DOWNLOAD_PATH` variable.
