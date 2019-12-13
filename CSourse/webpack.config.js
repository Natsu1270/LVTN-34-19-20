const path = require('path')

module.exports = {
    entry: {
        app: './CSourse/static/js/main.js'
    },
    mode: 'development',
    watch: true,
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'CSourse/static')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
			{
				test: /\.scss$/,
				use: ['style-loader', 'css-loader', 'scss-loader']
			}
        ]
    },
    resolve: {
        extensions: [
            '.js'
        ]
    }

}
