$.widget( "tagging_app.taggingApp", {
    options: {
        apiUrl: "tagging_app/"
    },

    _create: function() {
    },

    getCreationUrl: function(){
        return this.options.apiUrl+"tagged_item_creation";
    },

    getTagCreationUrl: function(){
        return this.options.apiUrl+"tag_creation";
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
    }
});
