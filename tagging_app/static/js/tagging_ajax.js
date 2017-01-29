$.widget( "tagging_app.taggingAjax", {
    options: {
        apiUrl: "/tagging_app/"
    },

    _create: function() {
    },

    getCreationUrl: function(){
        return this.options.apiUrl+"tagged_item_creation/";
    },

    getTagCreationUrl: function(){
        return this.options.apiUrl+"tag_creation/";
    },

    createTag: function(tagName, callback){
        $.post(this.getTagCreationUrl(), {name: tagName}, function(result){
            if(callback)callback(result);});
    },

    createTagForItem: function(tagName, objectId, contentType, callback){
        var thisWidget = this;
        this.createTag(tagName, function(result){
            $.post(thisWidget.getCreationUrl(), {tag: result.id, content_type: contentType, object_id: objectId},
                function(result){
                    if(callback)callback(result);
                }
            );
        });
    },

    getSetTagUlr: function(){
        return this.options.apiUrl+"set_tags/";
    },


    setTagForItem: function(tagName, objectId, contentType, callback){
        //tagName could be:
        //"": remove tags
        //"xx,yy": tag with "xx" and "yy"
        $.post(this.getSetTagUlr(), {tags: tagName, content_type: contentType, object_id: objectId},
            function(result){
                if(callback)callback(result);
            }
        );
    },

    setTag: function(tagName, objectId, callback){
        this.setTagForItem(tagName, objectId, $(this.element).attr("content_type"), callback)
    }
});
