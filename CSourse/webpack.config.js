const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
	context: __dirname,
	entry: {
        app: './CSourse/static/js/main.js'
    },
    mode: 'development',
    watch: true,
    output: {
        path: path.resolve(__dirname, 'CSourse/static/dist'),
		filename: '[name]-[hash].js',
    },
	devtool: "source-map",
	plugins: [
		new BundleTracker({filename: './CSourse/wepack-stats.json'})
	],
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
