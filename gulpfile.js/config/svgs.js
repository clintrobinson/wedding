var config = require('./')
,   fs     = require('fs')
,   path   = require('path')
,   argv   = require('yargs').argv;

/**
 * svgmin config object
 */
module.exports.svg = {
  src: config.sourceAssets + 'svgs/**/!(sprite)*.svg',
  spriteSrc: config.sourceAssets + 'svgs/**/(sprite)*.svg',
  dest: (argv.proto) ? config.prototypeAssets + 'svgs' : config.appAssets + 'svgs'
}

/**
 * svg2jade config object
 */
module.exports.svg2jade = {
  src: config.sourceAssets + 'jade_svgs/*.svg',
  dest: config.sourceDirectory + 'templates/_svgs/',
  options: {
    nspaces: 2,
    donotencode: true,
    bodyless: true
  }
}

