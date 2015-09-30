

/**
 * Default jQuery Enclosure
 */
(function (window, $) {
  'use strict';

  var LIFT;

  LIFT = {
    // variables
    clickType: ('ontouchstart' in document.documentElement ? 'touchstart' : 'click'),  // event type (if mobile use touch events)

    // init gets called by default, but we're just going to use it
    // to call our other functions to keep our individual modules
    // clean and compartmentalized
    init : function () {
      // ie. this.menu();
      $("input:radio[name=attending]").change(function() {
        var value = $(this).val();
        var attend_name = $('.attend_name').val();
        if(value == 'Yes'){
          if(attend_name != ""){
            $('.guest_name').attr("placeholder", attend_name + "'s Guest Name");
          }
          $(".guestfield").slideDown();
        } else if (value == 'No'){
          $(".guestfield").slideUp();
          $('.guest_name').val("");
        }
      });
    },

    anotherFunction : function () {

    },

    /**
     *  SAFE LOGGING
     *  Allows you to do `this.log(var)` or `LIFT.warn('warning message')`, etc. and you won't break < IE9 by accident)
     */

    log : function (message) {
      if (window.console) {
        console.log(message);
      }
    },

    error : function (message) {
      if (window.console) {
        console.error(message);
      }
    },

    warn : function (message) {
      if (window.console) {
        console.warn(message);
      }
    }

  };


  // DOM ready, let's DO DIS!
  $(document).ready(LIFT.init);

})(window, window.jQuery);

