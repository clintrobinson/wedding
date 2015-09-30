var config          = require('./')
,   webpack         = require('webpack')
,   webpackManifest = require('../lib/webpackManifest')
,   path            = require('path')
,   argv            = require('yargs').argv;

module.exports = function (env) {
  var jsDest
  ,   jsSrc  = config.sourceDirectory + 'js/';

  jsDest = (argv.proto) ? config.prototypeAssets + 'js/' : config.appAssets + 'js/'

  var webpackConfig = {
    // Entry will be the files created by Webpack,
    // the key is the name of the js file and it's
    // value is the "entry point" (source file) for
    // the javascript input
    src : jsSrc + '**',
    entry: {
      app:  [jsSrc + 'App.js'],
      modernizr: [config.sourceDirectory + 'bower/modernizr/modernizr.js']
    },

    output: {
      path: jsDest,
      filename: '[name].js',
      publicPath: (argv.proto) ? config.prototypeAssets + 'js/' : '/static/js/'
    },

    plugins: [
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "window.jQuery": "jquery",
        "GLOBAL": "./global"
      }),
      new webpack.DefinePlugin({
        DEBUG: (argv.dev || argv.proto) ? true : false
      }),
      new webpack.optimize.DedupePlugin(),
      new webpack.optimize.UglifyJsPlugin(),
      new webpack.NoErrorsPlugin()
    ],

    resolve: {
      extensions: ['', '.js', '.jsx', '.coffee'],
      modulesDirectories: ['node_modules', 'raw/bower', 'raw/js'],
      root: __dirname,

      // Without this alias, webpack will run into problems pathing to/finding our
      // "GLOBAL" js specified in the new webpack.ProvidePlugin() above
      alias: {
        global: path.join(__dirname, '../../raw/js/global.js')
      }
    },

    module: {
      loaders: [
        {
          test: /\.js$/,
          loader: 'babel-loader?stage=1',
          exclude: /node_modules/
        },
        {
          test: /\.coffee$/,
          loader: 'coffee-loader',
          exclude: /node_modules/
        }
      ]
    }
  }

  return webpackConfig
}