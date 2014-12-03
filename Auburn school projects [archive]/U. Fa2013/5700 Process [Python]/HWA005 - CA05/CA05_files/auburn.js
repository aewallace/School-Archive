/**
 * JQuery is the javascript library used in many places across canvas.  
 *
 * Add an additional change password link to the login screen.
 **/


$(document).ready(function(){
                  if(window.location.pathname.search('login')){
                  var new_link = $('<br/><br/><a href="http://www.auburn.edu/img/canvas/help/general/password/" title="change my password">Password Help</a>');
                  $('#login_forgot_password').parent().parent().append(new_link);
                  }
                  });