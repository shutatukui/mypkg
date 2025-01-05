# season_fish 
[![test](https://github.com/shutatukui/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/shutatukui/mypkg/actions/workflows/test.yml)

このRos2のパッケージは1～12月の月毎の旬の魚を表示するものです。
このパッケージは、情報を発信する```talker```ノードと受信、出力する```listener```ノードに構成されています。

# 動作環境
- Ubuntu 22.04.5 LTS
- Ros2: foxy


# 構成ノード
**```talker```ノード**
- 名称: ```fish_season.py```
  
**```listener```ノード**
- 名称: ```listener.py```
- テスト用ノード

# 使用方法
```
### talker ###

cd ros2_ws
ros2 run mypkg talker

### listener ###

cd ros2_ws
ros2 run mypkg listener

### 実行結果 ###

[INFO] [1736059685.782867606] [seasonal_fish_listener]: Received fish info: ブリ (Month: 1)
[INFO] [1736059686.778027671] [seasonal_fish_listener]: Received fish info: ブリ (Month: 1)
[INFO] [1736059687.778926655] [seasonal_fish_listener]: Received fish info: ブリ (Month: 1)

### 補足 ###

この結果は、datetimeによりパソコンの日付を読み取っている。よって、パソコンが1月ならばブリ
2月はフグ、3月はサワラ...実行結果は月によって変わる。

```

# ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

 ©　2025 Tsukui Shuta
