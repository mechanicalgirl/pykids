
$(document).ready(function () {
  

  // Allow the user to hide/show the menu if they're in a narrow viewport.
  $('.yk-toggle-menu').click(function (e) {
    e.preventDefault();
    var $menu = $('.yk-container-nav');
    var newText;
    $menu.toggleClass('yk-menu-collapsed');
    if ( $menu.hasClass('yk-menu-collapsed') ) {
      newText = 'Show menu';
    } else {
      newText = 'Hide menu';
    }
    $('.yk-toggle-menu').text(newText);
  });
  
  
  // If the "hide/show menu" link is visible, it means we're at a narrow
  // breakpoint, so the menu should be collapsed by default.
  if ( $('.yk-toggle-menu:visible').length ) {
    $('.yk-container-nav').addClass('yk-menu-collapsed');
  }
  
  // All the "answer" sections should toggle and be collapsed by default.
  $('pre.toggle').each(function (i, pre) {
    var $pre = $(pre);
    $pre.addClass('toggle-collapsed');
    
    $pre.click(function () {
      var shouldBeExpanded = $pre.hasClass('toggle-collapsed');
      $pre.toggleClass('toggle-collapsed', !shouldBeExpanded);
    });
    
  });
  
  
});



