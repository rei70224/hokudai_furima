var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: {
    js: './hokudai_furima/static/js/index.js',
    css: './hokudai_furima/static/css/index.scss',
  },
  output: {
      path: path.resolve('assets/bundles/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    rules: [
    　{
     　 test: /\.css$/,
     　 use: [ 'style-loader', 'css-loader' ]
  　  },
      {
        test: /\.(jpg|png)$/,
        loaders: 'url-loader'
      },
    ],
  },
}
