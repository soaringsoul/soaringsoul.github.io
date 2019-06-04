---
layout:     post
title:      "适合Pythoner的React入门教程"
subtitle:   "React 简明教程"
date:       2018-10-11 23:00:00
author:     "soaringsoul"
header-img: "img/ubuntu_login.png"
catalog: true
tags:
    - 技术翻译
---



之前一段时间一直在关注Github上的 plotly/dash这个开源项目，也使用过这个项目做过一个可视化的报告，比较便捷美观，更重要的是可以使用react自主定制组件并且可以转化为python的库来使用，这一点是我选择dash作为目前数据可视化的最优选择的主要原因。

dash 使用[dash-component-boilerplate](https://github.com/plotly/dash-component-boilerplate "dash-component-boilerplate")来自主定制组件，
dash-component-boilerplate基于React，因此要自主开发自己的组件库需要先学习一些关于React的入门知识。

本文即是dash官网上关于react入门介绍的一个翻译，初衷是翻译一下，既是一个学习的过程，也方便后面回头查阅。
原文链接：[https://dash.plot.ly/react-for-python-developers](https://dash.plot.ly/react-for-python-developers "React for Python Developers: a primer introduction")


# 简介 #
如果你是一个Dash 开发者，在某些时候你或许考虑过为dash开发一些自己的组件，你或许已经看过我们的源代码或者已经尝试使用了dash-component-boilerplate。

然而，如果你之前从有过Javascript或者React的编程经验，面对dash-component-boilerplate你肯定会非常困惑。

不过在你学习完这篇入门指南后，即使你从未使用过这些编程语言，你也应该可以习惯使用React和JavaScript来定制你的Dash组件了。好了，言归正传，让我们一起开始学习吧。

# JavaScript #
JavaScript是一种兼容目前所有浏览器的web编程语言，大多数web页面会使用它来与用户进行交互，自从诞生以来，经过漫长的发展，目前已经成为前端开发的标准语言。

如今，Javascript具有非常丰富的功能，可构建完美切合web的开发体验。
React
React由Facebook编写和维护，是一个用于构建用户界面的Javascript库，凭借其强大的响应式和声明式编程风格，在过去的几年里备受前端开发者的欢迎。

React的出现，使前端代码变得友好，便于阅读和理解，而且它的开发理念鼓励代码的模块化和可复用化。另外，React还有一个庞大而活跃的开源社区，发布了各式各样的UI组件，从滑动条到数据表，从下拉菜单到按钮，一应俱全。

理解**```React本质就是JavaScript```**非常关键。

React并非是一种新的编程语言，也不是一个需要学习多年才可以掌握的框架。它有一个相对较小的API供你学习，你只需要通过一些功能和范例就可以在你开始用它编写Web程序前先了解它。

尽管如此，对于所有陌生的编程语言都会有一个学习曲线，不过也不用担心，通过足够的练习和耐心你肯定可以掌握它的。


Dash在底层使用React来渲染使用Dash创建的Web页面，因为React允许用户在可管理自身状态的封装组件中编写用户界面，因此为Dash分离出部分代码就变得简单了（刚开始没看懂这句话，结合下文，应该是说Dash也可以像React一样将组件化）。

在这个入门教程的结尾，你将会看到，Dash组件和React组件可以1对1对进行映射。

# 安装所有依赖项 #

----------

让我们从设置Javascript的开发环境开始吧，我们将使用Node.js ,NPM，以及我们的dash-component-boilerplate去编写我们的第一个React程序。
## Node.js ##
Node.js是一个Javascript的运行环境，它允许你在浏览器之外运行Javascript代码，就像你可以在终端中运行Python代码一样，你可以通过```node my-code.js```在终端中运行你的JavaScript代码。即使你最终是打算在浏览器中运行你的代码，但是使用Node来进行开发还是会非常的方便。
## NPM ##
NPM是“Node Package Manage"的简称，主要用于安装包以及运行脚本。除了作为包管理器之外（不同于Python的pip),npm也允许你执行其他诸如运行脚本以及执行任务等操作。

例如你可以通过运行```npm init```来创建项目，可以通过```npm start```来启动项目，或者你也可以通过运行```npm run custom-script```来触发你的自定义脚本。

每个使用npm的项目都会有一个package.json的配置文件，所有的自定义脚本都在这个配置文件里定义。这个package.json文件类似于你在python中使用到的requirements.txt 和devRequirements.txt，你可以通过```npm install ```来安装，一如你在Python中使用```pip install -r requirements.txt```。

另外，package.json也包含了一个脚本部分，你可以在这里定义你的常用脚本程序。通常来说，查看package.json文件是检查一个项目使用到哪些scripts的快捷方式。

如果你使用过[dash-component-boilerplate](https://github.com/plotly/dash-component-boilerplate "dash-component-boilerplate"),你就会发现你需要设置一些React 样式的代码，以帮助你快速启动一个React开发环境，以完成构建用于Dash的React 组件。这些scripts将使用一系列的技术（如Babel,Webpack等）将我们编写的代码编译成一个可用于web的包。


* 安装Node.js，
*到the Node.js website下载最新版本，推荐安装LTS版本。
Node.js将在你的电脑上自动安装 npm
查看安装的node版本，使用node -v指令
* 查看安装的npm版本，使用npm -v


现在我们安装了Node.js，让我们一起按照[dash-component-boilerplate](https://github.com/plotly/dash-component-boilerplate "dash-component-boilerplate")中的操作指南来构建我们的组件吧。
# React 快速介绍 #
现在，让我们先看下我们的React 程序代码是什么样子的。在你最喜欢的IDE 里打开以下文件：

    src/lib/components/ExampleComponent.react.js

代码内容：

    import React, {Component} from 'react';
    import PropTypes from 'prop-types';
    import * as R from 'ramda';
    
    import {ExampleComponent} from '../lib';
    
    class App extends Component {
    
    constructor() {
        super();
        this.state = {
            value: ''
        }
        this.setProps = this.setProps.bind(this);
    }
    
    setProps(newProps) {
        this.setState(newProps);
    }
    
    render() {
        return (
            <div>
                <ExampleComponent
                    setProps={this.setProps}
                    {...this.state}
                />
            </div>
        
        )
    }
    }
    export default App;


没错！这就是我们的第一个React组件了！

事实上，我们的用户界面就是由这些“组件”组成，而且按照惯例，每个文件通常会有一个主组件。
这个项目通过在`src/demo/App.js`（演示应用程序）中导入ExampleComponent组件。
## JSX ##
你在React中看到的`<h1>`和`<div>`标签像极了HTML中的标签，但是它们却有着微小的差异。这类标签实际上就是采用了JSX的语法标准了，JSX由React团队开发，是JavaScfipt的扩展，可实现在JavaScfipt组件中使用类似HTML的标记。下面是JSX 标签和HTML标签主要的几个差异：

* `class` 关键字被`className`取代了，Dash中用法同React

* 在写HTML时我们用字符串来写内嵌风格，如

  `<h1 style="color: hotpink; font-size: 12px">Hello Dash</h1>`

  但是在React中我们使用具有驼峰风格的属性对象，eg:

  `<h1 style={{"color": "hotpink", "fontSize": "12px"}}>Hello Dash<h1>`

* 在JSX中，我们可以将变量嵌套到标记中，也可以在变量中嵌套变量，只需要将嵌套的变量放进`{}`中即可，例如：

​		render() {
​		    var myText = 'Hello Dash!';
​		    return (

		          <h1>{myText}</h1>
​		    );
​		}


* 除了可以使用类似 HTML 标签的`<h1>`和`<div>`,在React中还可以引用别的React的类，例如，在我们的`src/demo/
* `中，我们通过`<ExampleComponent>`的方式引用并渲染了`ExampleComponent`组件。

# JavaScript语言快速入门  #


## 变量声明

在使用JavaScript时，如果要声明变量，必须使用`let` 或`const`。

`const`用于声明不可修改的变量（译者注：一般用于定义全局变量，而且必须初始化），let则可自由定义。
eg:

    const color = 'blue';
    let someText = 'Hello World';
    let myText;
    myText = 'Hello Dash';
## 注释
* 单行注释使用`//`
* 多行注释使用`/**/`


## 字符串
在Javascript中，定义字符串时使用单引号或者双引号，无区别。

eg:

    const someString = 'Hello Dash';
    const anotherString = "Hello Dash";

## 字典
python中我们使用字典来保存键值对，JavaScript中则使用Objects，二者被实例化和访问的方式非常相似，
eg:

    const myObject = {"color": "blue", "size": 20};
    myObject['color']; // is blue
    myObject.color;  // another way to access the color variable

python中，字典的键可以是任何类型，但是在JavaScript中，键只能是字符口中。但是在Javascript中却可以允许省略键的引号，eg:

    const styleProperty = "color";
    const myObject = {[styleProperty]: "blue"};
    myObject.color;

## 列表

Python中的列表在Javascript中被称作数组（"arrays"），二者被实例化和被访问的方式是相同的，
eg:

	const myList = ["Hello", "Dash", "!"];
	myList[0];  // Hello
	myList[1];  // Dash
	myList[myList.length - 1]; // -1 references aren't allowed in JavaScript

## 分号（Semicolons）

JavaScript中，约定每个表达式以一个分号结尾，不是绝对必要，但惯例如此。

## Print Statements, Errors, and the Console

Javascript中使用`console.log`来打印语句至控制台中，eg `console.log("Hello Dash");`


因为Javascript 一般运行在 web 浏览器中，我们并不能像在python 终端中那样直接看到这些打印的语句，相反，我们可以在浏览器中的`dev tools console`中看到这些打印语句，访问console的流程大致如下：

* 1 在web页面点击右键
* 2 点击“查看网页源代码”
* 3 点击 “控制台”标签

你如果想亲自看一下，可以在示例组件中的`ExampleCOmponent`的`render`方法中添加一条 `console.log`语句，然后刷新页面再在浏览器中的控制台查看。

## if , for ,while

### if 

	if (color === 'red') {
	  console.log("the color is red");
	} else if (color === 'blue') {
	  console.log("the color is blue");
	} else {
	  console.log("the color is something else");
	}

### for 

	for (let i = 0; i < 10; i++) {
	  console.log(i);
	}

### while

	while let i = 0; while (i < 10) { i += 1; }

## 函数

在JavaScript中，函数一般可以用以下两种方式来定义：

* 新风格方式，eg:


		const add = (a, b) => {
		// The inside of the function
			const c = a + b;
			return c;
		}


`console.log(add(4, 6)); // 10`

* 传统方法，eg:
		
		function (a, b) {
		  // The inside of the function
		  const c = a + b;
		  return c;
		}

`console.log(add(4, 6)); // 10`

## 类

> 注意！类在JavaScript中是新语言功能， 从技术上讲，它们是名为ES6的新版JavaScript的一部分。 当我们构建我们的JavaScript代码时，可以使用一个名为Babel的工具，它可以将这些新语言的功能转化为旧版本的浏览器（如IE11)可以使用的简单的JavaScript

JavaScript中的类同Python中的类非常的相似，让我们来看一个示例，

* 先来看一下Python的类:

		class MyComponent(Component):
		    def __init__(self, a):
		        self.a = a;
		        super().__init__(a)
		
		    def render(this):
		        return self.a;

* 再让我们看看使用Javascript中定义类的方式：

		class MyComponent extends Component {
		    init() {
		        super();
		        this.a = a;
		    }
		
		    render() {
		        return this.a;
		    }
		}


## Importing and Exporting

在Python中，可以引用任意文件中的任意变量，在Javascript中则必须通过“导出”变量来明确指定我们想要“可导入”的变量。

* 如果我们仅仅想导入单个变量， 我们将这样写 ` export default:`

`some_file.js`:

		const text = 'hello world';
		export default text;

`another_file.js`:
	import text from './some_file.js';

* 如果我们想导入多个变量，我们可以这样写：
* `export : some_file.js`

	    const text = 'hello world';
	    const color = 'blue';
	    const size = '12px';
	    
	    export text;
	    export color;

再定义一个`another_file.js`来导入some_file.js中的多个变量，eg:

`import {text, color} from './some_file.js';  
// 注意在这里不能import size ,因为在some_file.js中没有export size`



## 标准库和Ramda

和Python不同，Javascript中的“标准库”非常小。在Plotly中，我们使用第三方库`ramda`进行常用的数据操作。

## Virtual DOM
再来看下`App.js`中的App组件，可以看到它是在代码的底部才被导出的，而且如果你打开`src/demo/index.js`文件，你会发现它是在这里被引用的（`import App from './App';`）,这样以来它才可以在`ReactDOM.render()`中调用。
`ReactDOM.render()` 方法只能在这里被调用而且只能调用一次。

`ReactDOM.render()`方法的功能即是将我们编写的React 代码，渲染为网页上的HTML，该方法在每个组件中只能被调用一次。
### `App.js`

	/* eslint no-magic-numbers: 0 */
	import React, {Component} from 'react';
	import PropTypes from 'prop-types';
	import * as R from 'ramda';
	
	import {ExampleComponent} from '../lib';
	
	class App extends Component {
	
	    constructor() {
	        super();
	        this.state = {
	            value: ''
	        }
	        this.setProps = this.setProps.bind(this);
	    }
	
	    setProps(newProps) {
	        this.setState(newProps);
	    }
	
	    render() {
	        return (
	            <div>
	                <ExampleComponent
	                    setProps={this.setProps}
	                    {...this.state}
	                />
	            </div>
	        )
	    }
	}
	
	export default App;

`index.js`

    import React from 'react';
    import ReactDOM from 'react-dom';
    import App from './App';
    
    ReactDOM.render(<App />, document.getElementById('root'));


## Classes

在这里（指`src/demo/App.js`）我们看到在App组件里定义了一个继承自React 的`Component`类的 `class`。这给我们提供了一些方法，例如在这里用到的`render`方法，它其实是被呈现它的组件调用的方法，在我们的示例中， `render()`由index.js中的`ReactDOM.render()`调用。注意`<App />`在`ReactDOM.render()`被调用的方式：被当做 JSX 标签调用。

## React.COmponet的其他方法
React提供的其他方法主要与组件状态管理有关。 我们已经使用了生命周期钩子，如`shouldComponentUpdate`和`componentDidMount`，它们允许您更好地指定组件何时以及如何更新。
对于这些方法，可以参考 [React documentation](https://reactjs.org/docs/state-and-lifecycle.html "React documentation")

# 我们自己的React 组件
## 创建样版组件
现在，让我们创建我们自己的组件吧！

在`src/lib/components/`目录下，创建一个文件：`TextInput.react.js`,写入以下代码并保存：

	import React, { Component } from 'react';
	
	class TextInput extends Component {
	  // here we'll define everything we need our TextInput component to have
	}

接下来，我们将在组件中编写一个`construtor`的方法。

在Python中，一个类构建函数通常使用`def __init__()`来在类中定义，但是在Javascript中我们使用`constructor()` 语法来构建。
在构建函数中，通过在组件中的Props上调用`super()`方法，并且设定一些`state`，看起来就像下面的示例：

	class TextInput extends Component {
	  constructor(props) {
	    super(props);
	    this.state = {
	      value: 'default'
	    }
	  }
	}

 `props` 是组件的属性，由组件的父级传递而来（类似Python中的继承）,并且可以作为props的属性。在构建函数中的props中调用`super()`，可以使我们在组件中使用`this.props`来使用props。 关键词 `this` 类似Python中的`self`。稍后，我们将给你演示如何传递`props`


## 定义 `render` 方法

接下来将为我们的新组件定义`render()`方法。在React中，我们声明了Ui组件，`render()`方法正是React想要渲染这些组件时调用的方法。


一个组件的`render()`方法可以返回一个基本的字符串，例如，`return "Hello, World!"`。当这个组件被使用时，它的`render()`方法被调用，并且将在页面上展示 "Hello, World!"。同样地，你也可以返回一个React元素（需要使用JSX指定）,React将渲染这个元素。

## 导出和导入一个组件

我们将继续`export`我们的组件，作为导出的默认值。这意味着我们无论在何时试图从这个文件中`import`一些变量或者元素时，如果我们不指定名字，我们将得到这个默认值作为导出的内容。eg:

	import React, { Component } from 'react';
	
	class TextInput extends Component {
	  constructor(props) {
	    super(props);
	    this.state = {
	      value: 'default'
	    }
	  }
	  render() {
	    return <input />
	  }
	}
	
	export default TextInput;

现在，让我们`import` 这个组件并且用于我们的APP组件中。

在`App.js`文件顶端添加 `import TextInput from '../lib/components/TextInput.react';`,然后在`render()`方法返回的某处，使用我们新建的`<TextInput />`组件。


见证奇迹的时刻到了！打开网页，我们得到了一个文本输入框！

![](https://i.imgur.com/ELogOon.jpg)


## 使用 setState()方法更新状态

然后，正如你看到的，这个文本输入框几乎没有用处，它没有与任何东西关联，也不能保存你键入的文本内容。


让我们改变一下我们在`TextInput`中的`render()`方法，在`<input />` 标签中设置HTML的`value`属性，设置代码是这样子的：`<input value='dash' />`。保存，然后我们现在应该可以看到我们的<input> 标签已经被设置为'dash'！

![](https://i.imgur.com/ixQ6sA3.jpg)

我们也可以将这个vaule的值设置为我们在`state`对象中定义的值，定义方式：`<input value={this.state.value} />`。

![](https://i.imgur.com/RU0wQA0.jpg)

JSX中，`{}`语法表示我们想要在JSX中写入Javascript内联语句，这样以来我们的`his.state.value`就可以被计算了。

Great!现在我们的输入项已经默认了。不过坏消息是我们的输入仍旧是没有多大用处，因为我们怎么尝试都不能更改我们的输入值。

通过以上方法，TextInput我们竟然不能在`<input/>` 输入框中输入内容，这多半会让你觉着很奇怪，不过呢，这却是与我们设定的React模型是一致的：在我们之前设定的`render`方法中，我们告诉React去渲染一个指定了值的`input`输入框。所以，React将忠诚地去执行这个渲染指令，不管我们现在是否还想在这个输入框中重新键入一些值。

为了确保在input输入框中显示我们输入的值，我们就必须让`value`变量随着我们输入的内容而同步变化。为了达到这一目的，我们可以实时监听输入的值并实时更新状态。代码如下：


	import React, { Component } from 'react';
	
	class TextInput extends Component {
	  constructor(props) {
	    super(props);
	    this.state = {
	      value: 'default'
	    }
	  }
	  handleInputChange = (e) => {
	    // get the value from the DOM node
	    const newValue = e.target.value;
	    // update the state!
	    this.setState({
	      value: newValue
	    })
	  }
	  render() {
	    return <input value={this.state.value} onChange={this.handleInputChange}/>
	  }
	}
	
	export default TextInput;


在这里，我们在输入组件里的`onChange`属性里编写了一个方法，可以在每次在输入框里输入内容里触发。这个方法中还有一个为了事件指定的参数`e`，在`e`上设置的`target.value`属性则正是我们需要的。这也是HTML DOM的工作方式，了解更多，点击 ["HTML <input type="text"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text "HTML <input type="text">")



接下来，我们使用了一个名为`setState()`的方法，它由`React.Component`提供。这个方法可以提交更新至我们的`state`对象。这个方法非常特殊，它将做下面这两件事：

1. 它将你提供的对象与当前 在`this.state`中的任何内容合并
2. 然后，重新渲染组件。也就是说，它将告诉React去使用`this.state`中的新数据再次调用组件的render方法。看看现在它是如何允许你在输入组件中输入内容的？我们也可以通过这样编写`render()`方法，来展示我们的状态：

		render() {
		  return <div>
		    <input value={this.state.value} onChange={this.handleInputChange} />
		    <p>{this.state.value}</p> // here we're displaying our state
		  </div>
		}

注意一下，不允许从`render()`中返回多个元素，但是带有子节点的元素是可以被返回的。

## Component props
我们也可以通过前面提到的`props`给我们的组件传递属性。

这与在组件上分配属性的工作方式相同，我们将通过向TextInput组件添加标签prop来演示！

让我们编辑APP.js中对<TextInput/>的调用：`<TextInput label='dash-input' />`。这表示我们现在在`TextInput`组件中有了一个名为`label`的`prop`可以使用了。

在TextInput中，我们可以通过`this.props`引用它。 让我们进一步扩展我们的`render()`方法，使它呈现我们的标签`prop`：

	render() {
	  return <div>
	    <label>{this.props.label}</label>
	    <input value={this.state.value} onChange={this.handleInputChange} />
	    <p>{this.state.value}</p>
	  </div>
	}

Props总是向下传递，但是你可以设置一个method作为prop，这样一个子对象就可以调用父对象的方法。获取更多相关的信息，可以移步 [React Docs](https://reactjs.org/docs/getting-started.html) 。

以上这些都仅仅是React的基本使用方法，如果你想了解更多 [React Docs](https://reactjs.org/docs/getting-started.html)是一个非常好的入门资料。


# 在Dash中使用React components

在Dash中可以使用大部分使用React构建的组件。
Dash在底层使用React,具体而言就是在`dash-renderer`中使用。

`dash-renderer`仅仅是一个基本的React app，它可以渲染你 Dash app中 `app.layout`定义的layout。它也负责将你在Dash中编写的调用方法分配给对应的组件并且保持一切为最新状态。

## Control the state in the parent


让我们修改前面的示例来控制父App组件中的状态，而不是TextInput组件中的状态。 让我们从将`state`中的`value`移到父组件开始。
在 `src/demo/App.js`中，添加状态并且转递`value`至组件：


	component App extends Component {
	  constructor() {
	    super(props)
	
	    this.state = {
	        value: 'dash'
	    };
	  }
	
	    render() {
	      return <TextInput label={'Dash'} value={this.state.value}/>
	    }
	}

在 `src/lib/components/TextInput.react.js`中，使用`value` prop代替`state`:


	component TextInput extends Component {
	  constructor() {
	    super(props)
	  }
	
	    render() {
	      return (
	          <div>
	            <label>{this.props.label}</label>
	            <input value={this.props.value}/>
	            <p>{this.props.value}</p>
	          </div>
	        )
	    }
	}


现在，像之前一样，`<input/>`在你输入内容时不会更新，我们需要更新组件中的`value`属性为我们键入的内容。为达到这一目的，我们将在父组件中定义定义一个函数，这个函数负责更新父组件中的`state`并且我们还要将这个函数向下传递给我们的组件，我们将这个函数命名为`setProps`:

	component App extends Component {
	  constructor() {
	    super(props)
	
	    this.state = {
	        value: 'dash'
	    };
	  }
	
	    setProps(newProps) {
	      this.setState(newProps);
	    }
	
	    render() {
	      return (
	        <TextInput
	          label={'Dash'}
	          value={this.state.inputValue}
	          setProps={this.setProps}
	        />
	    }
	}

并且在`TextInput`中,我们将在`inpupt`中的`value`发生变化 时调用这个函数，也就是说，当我们输入框中输入内容时：


	component TextInput extends Component {
	  constructor() {
	    super(props)
	
	  }
	
	    handleInputChange = (e) => {
	      const newValue = e.target.value;
	      this.props.setProps({value: newValue});
	    }
	
	    render() {
	      return (
	          <div>
	            <label>{this.props.label}</label>
	            <input value={this.props.value} onChange={this.handleInputChange}/>
	            <p>{this.props.value}</p>
	          </div>
	        )
	    }
	}


让我们一起看下，当我们在`<input>`中键入内容时，都发生了些什么：

1. 在我们在输入框中键入内容时，`handleInputChange` 被调用
2. `this.props.setProps`被调用，然后调用App组件中的`setState`方法
3. App组件中的`this.setState`被调用，它将更新App组件中的`this.state`并且隐式调用`App.render`方法.
4. 当`APP.render`被调用时，`App.render`会带着新的`properties`参数调用`TextInput.render`，并用这个新的`value`渲染`input/`。

在Dash app中， `dash-renderer`和`App.js`非常相似。

----------
未完待续……
