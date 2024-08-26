const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',  // Your backend server URL
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
        onProxyReq: (proxyReq, req, res) => {
          proxyReq.setHeader('Access-Control-Allow-Origin', '*');
        },
        onProxyRes: (proxyRes, req, res) => {
          proxyRes.headers['Access-Control-Allow-Origin'] = '*';
        }
      }
    }
  }
})

