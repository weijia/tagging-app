$.widget( "tagging_app.taggingApp", {
    options: {
        apiUrl: "tagging_app/",
        tipElem: null
    },

    initTipElem: function(){
        var thisWidget = this;
        if($("#tagTip")){
            this.options.tipElem = $('<div id="tagTip" style="display:none">'+
                    '<input id="tagInput" objectId="" contentType="" value="" /><button>Submit</button>'+
                    '</div>');
            this.options.tipElem.taggingAjax();

            $("button", this.options.tipElem).click(function(e){
    //            console.log(e.target);
                var divElem = $(e.target).parent();
                var inputElem = $("input", divElem);
                $("#tagTip").taggingAjax("setTagForItem", inputElem.val(), inputElem.attr("objectId"),
                                            inputElem.attr("contentType"));
                thisWidget.element.qtip("hide");
            });

        }
    },

    _create: function() {
        this.initTipElem();
        this.addHoverMenu(this.element);
        this.addClickMenu(this.element);
    },

    addHoverMenu: function(element){
        var localElement = element;
        var thisWidget = this;
        element.qtip({
            content: {
                text: function(event, api) {
//                    return 'Loading...'; // Set some initial text
//                    return localElement.attr("tags");
                      var htmlTip = $("#tagInput", thisWidget.options.tipElem);
                      htmlTip.attr("objectId", localElement.attr("objectId"));
                      htmlTip.attr("contentType", localElement.attr("contentType"));
                      htmlTip.attr("value", localElement.attr("tags"));
////                      var htmlTip = $('<input class="tag-input" objectId="'+localElement.attr("objectId")+
////                                '" contentType="' + localElement.attr("contentType") + '" '+
////                                'value="'+localElement.attr("tags")+'"/>');
////                       $("body").append(htmlTip);
//                       htmlTip.tagsInput();
////                       htmlTip.tagator();
                       return thisWidget.options.tipElem;
                }
            },
            position: {
                target: 'mouse', // Use the mouse position as the position origin
                adjust: {
                    // Don't adjust continuously the mouse, just use initial position
                    mouse: false
                }
            },
            hide: 'unfocus',
            style: 'qtip-wiki'
         });
        return;
    },

    addClickMenu: function(element){

    }

});
