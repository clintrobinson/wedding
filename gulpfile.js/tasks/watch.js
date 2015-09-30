var gulp    = require('gulp')
,   images  = require('../config/images')
,   svgs    = require('../config/svgs')
,   sass    = require('../config/sass')
,   jade    = require('../config/jade')
,   argv    = require('yargs').argv
,   webpack = require('../config/webpack')(process.env.NODE_ENV)
,   watch   = require('gulp-watch');

//gulp.task('watch', ['browserSync'], function() {
gulp.task('watch', function() {

  watch(images.src,        function() { gulp.start('images'); });
  watch(svgs.svg.src,      function() { gulp.start('svgs'); });
  watch(svgs.svg2jade.src, function() { gulp.start('svg2jade'); });
  watch(webpack.src,       function() { gulp.start('eslint', 'webpack'); });

  // We set 'sass' as a dependency of 'cssmin', so
  // we actually call cssmin when sass changes. This
  // means SASS runs, and then our CSSMIN task.
  watch(sass.src,          function() { gulp.start('cssmin'); });

  if (argv.proto) {
    global.jadeFirstCompile = true
    watch(jade.src,        function() { gulp.start('jade'); });
  }
});
