/**
 * Webpack
 * ----------------------------------------------------
 * Webpack splits our javascript into modules that makes
 * it a lot easier to maintain large javascript projects.
 */
var assign       = require('object-assign')
,   config       = require('../config/webpack')(process.env.NODE_ENV)
,   gulp         = require('gulp')
,   logger       = require('../lib/compileLogger')
,   webpack      = require('webpack')
,   browserSync  = require('browser-sync')

gulp.task('webpack', function (callback) {
  webpack(config, function(err, stats) {
    logger(err, stats)
    callback()
  })
});