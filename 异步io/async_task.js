function foo() {
    console.log("begin")
    setTimeout(()=>{
        console.log("hello")
    }, 0)
    afoo()
    elapse(2)
    console.log("done")
}

async function afoo(){
    console.log("hello")
}

function elapse(n) {
    let start = new Date().getTime()
    let now = start
    while(now < start + n*1000) {
        now = new Date().getTime()
    }
}

function main() {
    console.log("begin")
    aysnc_elapse(2)
    console.log("done")
}

async function aysnc_elapse(n) {
    let start = new Date().getTime()
    let now = start
    while(now < start + n*1000) {
        now = new Date().getTime()
    }
    console.log("counting ", n, " done")
}

main()