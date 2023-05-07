# Flagapp

## Attachment:

[flagapp.apk](./flagapp.apk)

## Description

```A simple app to generate the flag```

## Solution

An APK file is given, after unziping it and looking inside it wen can fide some Flutter files, so the app was made using Flutter

Let's start by runing the app using a mobile or an android emulator

It's just a simple app with one button, after clicking the button it generates the flag but it's not displayed, now we know that flag is generated in the background

After searching in internet to learn about reverse engineering Android applications made using Flutter, we will find it's a challenging so we need to find a simpler way

Since the flag is generated in the background if we find a way to leak the content of the memory of the process we will find the flag

After searching in the internet we can find a tool `pmdump` (you can find it via this [Link](https://github.com/friendlyJLee/pmdump)) which uses `adb` and does exactly what we need, but it works only on rooted phones

In this case to avoid problems with the mobile if it's not already rooted, we can just use an emulator

Now what is left is to follow the instructions of the tool

1. Run adb in root mode

```bash
adb root
```
2. Copy pmdump to the mobile after choosing the correct file for the mobile architecture from the files which can be found inside the project in `pmdump_prebuilt_in`

```bash
adb push pmdump.OS.ARCHITECTURE /data/pmdump
```

3. Find the process id of the app

```bash
adb shell ps | grep flagapp
```

4. Dump the memory content of the process

```bash
adb shell

/data/pmdump PID
```

5. Search the flag inside the dump

```bash
grep shellmates /data/output_pmdump.bin
```

## Flag

`shellmates{dYn4M1c_4N4lys1S_1n_FLuTt3r_1s_d0P3}`