# rpimotortest

Small applications using Nema stepper motor and L298N motor driver.

## Environment

This repository is based on [RpiMotorLib tutorial](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/Nema11L298N.md).

### Hardware

- Raspberry Pi 3B+
- [Nema 11 stepper motor](https://www.pololu.com/product/1205/resources)
- [L298N motor controller](https://components101.com/modules/l293n-motor-driver-module)

The pin connections are the following. Note that pin number of L298N is based on the RpiMotorLib tutorial.

| Pi | L298N |
|:---|:---|
| 2 (5V) | 6 (5V in) |
| 6 (GND) | 5 (GND) |
| 11 (GPIO17) | 8 (IN1) |
| 12 (GPIO18) | 9 (IN2) |
| 13 (GPIO27) | 10 (IN3) |
| 15 (GPIO22) | 11 (IN4) |

| L298N | Nema |
|:---|:---|
| 1 (OUT1) | Green |
| 2 (OUT2) | Blue |
| 13 (OUT3) | Black |
| 14 (OUT4) | Red |

### Software

- Python 3.9 (see `.python-version` file)
- OS versions are the following

```console
$ cat /etc/os-release
PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
NAME="Raspbian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
$ uname -a
Linux raspberrypi 4.19.66-v7+ #1253 SMP Thu Aug 15 11:49:46 BST 2019 armv7l GNU/Linux
```

## Usage

Prepare packages:

```console
pip install -r requirements.txt
```

And run any file with your Python.

## References

- [RpiMotorLib](https://github.com/gavinlyonsrepo/RpiMotorLib)
  - This repository is based on this repository
- [Qiita: [Raspberry Pi] ラズパイでステッピングモータ制御](https://qiita.com/zoo_dj/items/0c7f632967e266bac64a) (ja)
