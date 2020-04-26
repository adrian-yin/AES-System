// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
  },
  extends: [
    // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
    // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
    'plugin:vue/essential', 
    // https://github.com/standard/standard/blob/master/docs/RULES-en.md
    'standard'
  ],
  // required to lint *.vue files
  plugins: [
    'vue'
  ],
  // add your custom rules here
  rules: {
    // allow async-await
    'generator-star-spacing': 'off',
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    // 语句强制分号结尾
    'semi': [0],
    // 允许最多5个空行
    'no-multiple-empty-lines': [0, {"max": 5}],
    'no-unused-vars': [2, {
        // 允许声明未使用变量
        'vars': 'local',
        // 参数不检查
        'args': 'none'
    }],
    // 禁止行内备注
    'no-inline-comments': 0,
    // 缩进
    'indent': 'off'
  }
}
