function HTTP() {};
HTTP.prototype.get = function() {
    function makeGet(path) {
        return function(){
            return 'GET ' + this.url + '/' + path;
        };
    }

    Array.prototype.forEach.call(arguments, function(name){
        this[name] = makeGet(name);
    }, this);
};

HTTP.prototype.method_missing = function(name) {
    this.constructor.prototype.get(name);
    return this.dot.apply(this, arguments);
};
