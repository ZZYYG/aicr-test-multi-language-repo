/**
 * 配置管理器模块
 */

class ConfigManager {
  /**
   * 创建配置管理器
   * @param {string} name - 配置名称
   * @param {Object} defaultConfig - 默认配置
   */
  constructor(name, defaultConfig = {}) {
    this.name = name;
    this.createdAt = new Date();
    this.defaultConfig = defaultConfig;
    this.currentConfig = { ...defaultConfig };
    this.history = [];
  }
  
  /**
   * 更新配置
   * @param {Object} newConfig - 新配置对象
   * @returns {Object} 更新后的完整配置
   */
  updateConfig(newConfig) {
    // 保存历史记录
    this.history.push({
      timestamp: new Date(),
      config: { ...this.currentConfig }
    });
    
    // 更新配置
    this.currentConfig = {
      ...this.currentConfig,
      ...newConfig
    };
    
    return this.currentConfig;
  }
  
  /**
   * 重置为默认配置
   * @returns {Object} 默认配置
   */
  resetToDefault() {
    this.history.push({
      timestamp: new Date(),
      config: { ...this.currentConfig },
      action: "reset"
    });
    
    this.currentConfig = { ...this.defaultConfig };
    return this.currentConfig;
  }
  
  /**
   * 获取配置值
   * @param {string} key - 配置键
   * @param {*} defaultValue - 如果键不存在时的默认值
   * @returns {*} 配置值
   */
  get(key, defaultValue = null) {
    return key in this.currentConfig 
      ? this.currentConfig[key] 
      : defaultValue;
  }
}

// 示例用法
const defaultAppConfig = {
  theme: "light",
  language: "zh-CN",
  notifications: true,
  autoSave: true
};

const configManager = new ConfigManager("应用配置", defaultAppConfig);
console.log("初始配置:", configManager.currentConfig);

// 更新配置
configManager.updateConfig({
  theme: "dark",
  autoSave: false
});
console.log("更新后配置:", configManager.currentConfig);
