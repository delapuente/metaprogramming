Object.prototype.method_missing = function() {
    throw 'NoMethodError';
};

Object.prototype.dot = function(name) {
    var args = Array.prototype.slice.call(arguments, 1);
    var f = this[name];
    if (!f) {
        args.splice(0, 0, name);
        return this.method_missing.apply(this, args);
    } else {
        return f.apply(this, args);
    }
};
