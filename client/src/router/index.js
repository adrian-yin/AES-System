import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main'
import Begin from '@/views/Begin'
import Login from '@/views/Login'
import Register from '@/views/Register'
import UserMain from '@/views/UserMain'
import History from '@/views/History'
import New from '@/views/New'
import Result from '@/views/Result'
import HelloWorld from '@/components/HelloWorld'
import store from '../store'

Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        {
            path: '/',
            name: 'HelloWorld',
            component: HelloWorld,
            meta: {
                required: true,
                title: 'HelloWorld'
            }
        },
        {
            // 主页面
            path: '/main',
            name: 'Main',
            component: Main,
            meta: {
                required: true,
                title: '主页面'
            },
            children: [
                {
                    // 用户主页
                    path: '/main/usermain',
                    name: 'UserMain',
                    component: UserMain,
                    meta: {
                        required: true,
                        title: '用户主页'
                    }
                },
                {
                    // 历史记录
                    path: '/main/history',
                    name: 'History',
                    component: History,
                    meta: {
                        required: true,
                        title: '历史记录'
                    }
                },
                {
                    // 新建评分
                    path: '/main/new',
                    name: 'New',
                    component: New,
                    meta: {
                        required: true,
                        title: '新建评分'
                    }
                },
                {
                    // 一进main初始显示usermain
                    path: '',
                    component: UserMain,
                    meta: {
                        required: true,
                        title: '用户主页'
                    }
                }
            ]
        },
        {
            // 登陆页面
            path: '/login',
            name: 'Login',
            component: Login,
            meta: {
                required: false,
                title: '登录'
            }
        },
        {
            // 注册页面
            path: '/register',
            name: 'Register',
            component: Register,
            meta: {
                required: false,
                title: '注册'
            }
        },
        {
            // 结果界面
            path: '/result',
            name: 'Result',
            component: Result,
            meta: {
                required: true,
                title: '评分结果'
            }
        },
        {
            // 首页
            path: '/begin',
            name: 'Begin',
            component: Begin,
            meta: {
                required: false,
                title: '首页'
            }
        }
    ]
})

// 全局前置守卫，判断用户是否登陆，未登陆跳转至登陆页面
router.beforeEach((to, from, next) => {
    // 自动添加title
    if (to.meta.title) {
        document.title = to.meta.title;
    }
    // 路由中定义的是否需要登陆权限
    if (to.meta.required) {
        if (store.state.token) {
            next();
        } else {
            if (sessionStorage.getItem('token')) {
                store.state.token = sessionStorage.getItem('token');
                next();
            } else {
                // 跳转到登陆页面
                next({
                    path: '/begin',
                    query: { redirect: to.fullpath }
                })
            }
        }
    } else {
        next();
    }
})

export default router;
