<template>
    <div class="container">
        <div v-for="(item, key, index) in suggestion" :key="index" class="each-error-shell-div">
            <div
                class="error-content-info"
            >
                <div class="word-revise-div">
                    <div class="Checkstyle__CorrectWordContent-an9z37-40 ehNdGM">
                        <span
                            class="unfixed Checkstyle__CorrectWord-an9z37-44 eUmdmJ"
                            style="font-size: 30px; width: 100px"
                        >{{key}}</span>
                    </div>
                    <div class="explaination" v-for="sitem in item.main" :key="sitem.sense">
                        <span class="meaning">意思：<span>{{sitem.sense}}</span></span><br />
                        <span class="example" v-if="sitem.examples[0]">例句：<span>{{sitem.examples[0][0]}}</span></span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
    export default {
        name: 'Vocabulary',
        props: {
            suggestion: {
                type: Object
            }
        },
        watch: {
            suggestion (val) {}
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
    background-color: #f9f9fb;
    min-width: 600px;
    overflow-x: auto;
    text-align: center;
    margin: 0 auto;
    width: 100%;
    // display: flex;
    // flex: 1;
    min-height: 100%;
    // justify-content: center;
}
.error-content-info {
    background-color: rgb(255, 255, 255);
    box-shadow: rgba(191, 204, 230, 0.75) 0px 10px 30px;
    padding: 10px 10px 10px;
    text-align: center;
    overflow: auto;
    border-radius: 5px;
    margin: 20px 50px;
    width: 700px;
}
.error-content {
    white-space: pre-wrap;
    line-height: 20px;
    font-size: 16px;
    color: rgb(132, 140, 163);
    cursor: pointer;
    text-align: left;
}
.fsReJu {
    min-width: 40px;
}
.ntLBp {
    display: block;
    height: 18px;
    font-size: 13px;
    line-height: 18px;
    color: rgb(178, 184, 201);
    margin-bottom: 8px;
}
.gKCJOw {
    white-space: pre-wrap;
    font-size: 30px;
    line-height: 33px;
    color: rgb(84, 89, 101);
    position: relative;
    display: inline-block;
}
.gKCJOw::after {
    content: "";
    top: 14.4px;
    display: block;
    height: 3px;
    position: absolute;
    width: 100%;
    background: rgb(238, 113, 153);
}
.eUmdmJ {
    display: inline-block;
    font-size: 24px;
    line-height: 33px;
    color: rgb(84, 89, 101);
    white-space: pre-wrap;
}
.word-revise-div {
    // display: flex;
    margin-top: 20px;
}
.right-icon-1 {
    width: 20px;
    height: 59px;
    margin: 0px 20px;
    padding-top: 30px;
    font-size: 24px;
    color: #b2c0d6;
}
</style>

<style>
.quillEditor p {
    font-weight: 4 00;
    font-family: Akkurat Std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Helvetica Neue, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 2rem !important;
    font-size: 1.125rem !important;
}
.explaination{
    color: #0F78FB;
    font-size: 16px;
    padding: 15px 30px;
    text-align: left;
}
</style>
