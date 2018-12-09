# py-kaomoji
Kaomoji library for Python

## What's py-kaomoji
This is a Kaomoji library for Python for Japanese.
You can find some cute kaomojis.

## Getting started
Install with `pip`.

```
pip install py-kaomoji
```

## How to use
Let's start with importing kaomoji library.
```
from kaomoji import kaomoji
```

You can get a random kaomoji string with `kao()`.
```
kao = kaomoji.Kaomoji()
kao()
> '(ヾﾉヾﾉヾﾉヾﾉヾﾉ･ω･`)ヾﾉｼﾞｪｯﾄｽﾄﾘｰﾑﾅｲﾅｲ'
```

Or, you can get several random kaomojis with `random_kaomoji()`.
```
kao.random_kaomoji(n=3)
> 'ピース(≧▽≦)v ⊂⌒っ´ｰωｰ)っ.。o○ (⊃д∩)'
```

You can also specify your kaomoji emotion.

```
kao.kaomoji("たのしい")
> "たのしい！✌('ω'✌ )三✌('ω')✌三( ✌'ω')✌"
```

The list of emotions you can express can be found with `get_kao_list()`.

```
kao.get_kao_list()
> 'あおり',
> 'あげ',
> 'あせ',
> 'あたふた',
> ...
```

If you feel like you need a party, you can run `super_kaomoji()`.

```
kao.super_kaomoji()
> 'てへぺろ！(*ゝωб) (((o(*ﾟ▽ﾟ*)o))) (´っω-).｡oO ･ﾟ･(ﾉд<)･ﾟ･ ｳｪ―ﾝ (〃l _ l) ヽ(｡ゝω･)ﾉ （＞ヮ＜*） =͟͟͞͞ (¦3[▓▓]'
```

If you don't think it's good enough, then just get `all_kaomoji()`.

```
kao.all_kaomoji()
> !!!!!!!!!!!!!!!
```

## License
This sample code is licensed under the [MIT License](https://github.com/shibuiwilliam/py-kaomoji/blob/master/LICENSE).