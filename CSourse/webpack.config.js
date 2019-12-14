const path = require('path');

module.exports = {
    entry: {
        app: './CSourse/static/js/main.js'
    },
    mode: 'development',
    watch: true,
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'CSourse/static/dist')
    },
	devtool: "source-map",
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
			{
				test: /\.scss$/,
				use: ['style-loader', 'css-loader?url=false', 'sass-loader']
			},
			{
				test: /\.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/, // For Font Awesome
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: '[name].[ext]',
                        outputPath: 'fonts/',    // where the fonts will go
                    }
                }]
			},
			{
				test: /\.(jpg|png|jpge)$/,
				use: ['file-loader']
			}
        ]
    },
    resolve: {
        extensions: [
            '.js'
        ]
    }

};
