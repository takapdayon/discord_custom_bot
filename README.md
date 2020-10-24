# LOL用Custom BOTです

discordにてlol customする際に使用していただければと思います。

# install
こちらからどうぞ<br>
[CustomBOT](https://discord.com/oauth2/authorize?client_id=575692856178769951&permissions=0&scope=bot)

# Usage

## !cus
単純に今いるメンバーを半分に分けます。
10人以上の場合は、観戦者となります。
#### DEMO
```
!cus

-チーム1------------------------------
Player1
Player7
Player5
Player3
Player9
-チーム2------------------------------
Player2
Player4
Player6
Player8
Player10
```

## !!cus
上記にlaneをつけて分けます。
#### DEMO
```
!!cus

-チーム1------------------------------
Top: Player1
Jg: Player7
Mid: Player5
Adc: Player3
Sup: Player9
-チーム2------------------------------
Top: Player2
Jg: Player4
Mid: Player6
Adc: Player8
Sup: Player10
```


## !!!cus
上記にchampもつけます。
#### DEMO

```
!!!cus

-チーム1------------------------------
Top: Kled Player1
Jg: Gragas Player7
Mid: Brand Player5
Adc: Soraka Player3
Sup: Kaisa Player9
-チーム2------------------------------
Top: Orianna Player2
Jg: Janna Player4
Mid: Shen Player6
Adc: Blitzcrank Player8
Sup: Talon Player10
```

## !cuslist
## コマンド name1 name2 ...
!cuslistでボイスチャンネル内のメンバー一覧を返します
また、上記3つのコマンドの後スペース区切りで名前を入れてもらうとそのメンバーを除外して
動作します
```
!cuslist

Player1
Player7
Player5
Player3
Player9
Player2
Player4
Player6
Player8
Player10

!cus Player1 Player10

-チーム1------------------------------
Player7
Player5
Player3
Player9
-チーム2------------------------------
Player2
Player4
Player6
Player8
```