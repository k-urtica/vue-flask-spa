# vue-flask-spa
Vue.jsとFlaskを使用したSPAプロジェクトテンプレート。

# 必要ツール

- [Vue-CLI](https://cli.vuejs.org/)
- [pipenv](https://pipenv-ja.readthedocs.io/ja/translate-ja/)

## 開発環境
開発時はフロントエンド側で開発サーバーを起動することで、ホットリロードが有効になります。

```yarn
yarn serve
```

バックエンド側Flaskは以下のコマンドで開発用サーバーで起動します。

```python
py run.py
```

開発時、フロントエンドサーバーからバックエンドサーバーへのAPIはvue.configの設定でflaskの5000ポートへプロキシさせています。

```
    proxy: {
      "/api*": {
        // /パスが /api～ のrequestはflaskへ転送させる
        target: "http://127.0.0.1:5000/"
      }
    }
```

## プロダクション環境
プロダクション環境として、herokuを想定してデプロイする手順です。

herokuプロジェクトのSettingsの「Buildpacks」で`node.js`と`python`を追加しておきます。

package.jsonに下記のコマンドを追記しているため、herokuへデプロイした際に、vueの依存ライブラリがインストールされた後にビルドまでされます。  
その後に`Pipfile`の依存ライブラリがインストールされて`Procfile`に従って、web dynoでgunicornが起動します。

```
  "postinstall": "yarn build"
```

※つまるところ、herokuへデプロイするだけでOKです。