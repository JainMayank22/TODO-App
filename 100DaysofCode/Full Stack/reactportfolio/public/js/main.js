$(window).on('load', function() {

    $('.level-bar-inner').each(function() {

        var itemWidth = $(this).data('level');

        $(this).animate({
            width: itemWidth
        }, 800);

    });

});


function TxtType(el, toRotate, period) {
  debugger;
  var obj={};
        obj.toRotate = toRotate;
        obj.el = el;
        obj.loopNum = 0;
        obj.period = parseInt(period, 10) || 2000;
        obj.txt = '';
   tick(obj);
        obj.isDeleting = false;

    };

function tick(obj){
  debugger;
   var i = obj.loopNum % obj.toRotate.length;
        var fullTxt = obj.toRotate[i];

        if (obj.isDeleting) {
        obj.txt = fullTxt.substring(0, obj.txt.length - 1);
        } else {
        obj.txt = fullTxt.substring(0, obj.txt.length + 1);
        }

        obj.el.innerHTML = '<span class="wrap">'+obj.txt+'</span>';


        var delta = 200 - Math.random() * 100;

        if (obj.isDeleting) { delta /= 2; }

        if (!obj.isDeleting && obj.txt === fullTxt) {
        delta = obj.period;
        obj.isDeleting = obj;
        } else if (obj.isDeleting && obj.txt === '') {
        obj.isDeleting = false;
        obj.loopNum++;
        delta = 500;
        }

        setTimeout(function() {
        tick(obj);
        }, delta);
}


    window.onload = function() {
        var elements = document.getElementsByClassName('typewrite');
        for (var i=0; i<elements.length; i++) {
            var toRotate = elements[i].getAttribute('data-type');
            var period = elements[i].getAttribute('data-period');
            if (toRotate) {
              TxtType(elements[i], JSON.parse(toRotate), period);
            }
        }
    };

jQuery(document).ready(function($) {


    /*======= Skillset *=======*/

    $('.level-bar-inner').css('width', '0');



    /* Bootstrap Tooltip for Skillset */
    $('.level-label').tooltip();


    /* jQuery RSS - https://github.com/sdepold/jquery-rss */

    $("#rss-feeds").rss(

        //Change this to your own rss feeds
        "https://feeds.feedburner.com/TechCrunch/startups",

        {
        // how many entries do you want?
        // default: 4
        // valid values: any integer
        limit: 3,

        // the effect, which is used to let the entries appear
        // default: 'show'
        // valid values: 'show', 'slide', 'slideFast', 'slideSynced', 'slideFastSynced'
        effect: 'slideFastSynced',

        // will request the API via https
	    // default: false
	    // valid values: false, true
	    ssl: true,

        // outer template for the html transformation
        // default: "<ul>{entries}</ul>"
        // valid values: any string
        layoutTemplate: "<div class='items'>{entries}</div>",

        // inner template for each entry
        // default: '<li><a href="{url}">[{author}@{date}] {title}</a><br/>{shortBodyPlain}</li>'
        // valid values: any string
        entryTemplate: '<div class="item"><h3 class="title"><a href="{url}" target="_blank">{title}</a></h3><div><p>{shortBodyPlain}</p><a class="more-link" href="{url}" target="_blank"><i class="fas fa-external-link-alt"></i>Read more</a></div></div>'

        }
    );

    /* Github Calendar - https://github.com/IonicaBizau/github-calendar */
    new GitHubCalendar("#github-graph", "IonicaBizau");


    /* Github Activity Feed - https://github.com/caseyscarborough/github-activity */
    GitHubActivity.feed({ username: "mdo", selector: "#ghfeed" });


});
