## Implementing *fullpagejs*

[Documentation](https://github.com/alvarotrigo/fullPage.js/)

See United Way page for working example

- Base Code JS

    // fullPage.js functionality
    // Credit to alvarotrigo https://github.com/alvarotrigo/fullPage.js
    var $header_top = $('.header-top');
    var $nav = $('nav');
    $header_top.find('a').on('click', function() {
    $(this).parent().toggleClass('open-menu');
    });
    $('#fullpage').fullpage({
    sectionsColor: [
        SECTION_COLORS (either as hex or vars)
    ],
    sectionSelector: '.vertical-scrolling',
    navigation: true,
    slidesNavigation: true,
    controlArrows: false,
    bigSectionDestination: 'top',
    scrollOverflow: true,
    paddingTop: '8rem',
    fixedElements: '.footer',
    anchors: ['firstSection', 'secondSection', 'thirdSection', 'fourthSection', 'fifthSection', 'sixthSection', 'seventhSection'],
    menu: '#menu',
    
    afterLoad: function(anchorLink, index) {
        // $header_top.css('background', 'rgba(0, 47, 77, .3)');
        $header_top.css('background', 'rgba(16, 22, 127, 1)');
        $nav.css('background', 'rgba(0, 47, 77, .25)');
        if (index == 5) {
            $('#fp-nav').hide();
        }
    },
    
    onLeave: function(index, nextIndex, direction) {
        if(index == 5) {
        $('#fp-nav').show();
        }
    },
    });

- Base Code HTML

    <div id="fullpage">
        <div class="section">One</div>
        <div class="section">
            <div class="slide" data-anchor="slide1">Two 1</div>
            <div class="slide" data-anchor="slide2">Two 2</div>
        </div>
        <div class="section">Three</div>
        <div class="section">Four</div>
    </div>