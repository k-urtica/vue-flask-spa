module.exports = {
  outputDir: "dist",
  assetsDir: "static", // 静的アセット出力先(outputDirに対する相対パス)
  devServer: {
    contentBase: "./public",
    proxy: {
      "/api*": {
        // /パスが /api～ のrequestはflaskへ転送させる
        target: "http://127.0.0.1:5000/"
      }
    }
  }
};
