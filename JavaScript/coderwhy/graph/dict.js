// 创建字典的构造函数
function Dictionary() {
  // 字典属性
  this.items = {}

  // 字典操作方法
  // 在字典中添加键值对
  Dictionary.prototype.set = function (key, value) {
    this.items[key] = value
  }

  // 判断字典中是否有某个key
  Dictionary.prototype.has = function (key) {
    return this.items.hasOwnProperty(key)
  }

  // 从字典中移除元素
  Dictionary.prototype.remove = function (key) {
    // 1 判断字典中是否含有此key
    if (!this.has(key)) return false

    // 2 删除key
    delete this.items[key]
    return true
  }

  // 根据key获取value
  Dictionary.prototype.get = function (key) {
    return this.has(key) ? this.items[key] : undefined
  }

  // 获取所有keys
  Dictionary.prototype.keys = function () {
    return Object.keys(this.items)
  }

  // size方法
  Dictionary.prototype.size = function () {
    return this.keys().length
  }

  // clear方法
  Dictionary.prototype.clear = function () {
    this.items = {}
  }
}