# season_fish 
[![test](https://github.com/shutatukui/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/shutatukui/mypkg/actions/workflows/test.yml)

このRos2のパッケージは1～12月の月毎の旬の魚を表示するものです。   


また、これは端末を２つに分けて使用します。

# 動作環境
- Ubuntu 22.04.5 LTS

# ROS2バージョン
- ROS2 Humble


# 構成ノード
**```talker```ノード**
- 名称: ```fish_season```
  
**```listener```ノード**
- 名称: ```listener```
- テスト用ノード

# 使用方法
```
### 端末1 ###

$ros2 run mypkg talker

```

```
### 端末2 ###

$ros2 topic echo /person

### 実行結果 ###

name: ブリ
age: 1
---
name: ブリ
age: 1
---
name: ブリ
age: 1
---

### 補足 ###

この結果は、datetimeによりパソコンの日付を読み取っている。よって、パソコンが1月ならばブリ
2月はフグ、3月はサワラ...実行結果は月によって変わる。

```

# ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

 ©　2025 Tsukui Shuta
