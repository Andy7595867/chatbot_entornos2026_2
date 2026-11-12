const prompt = "hola que es la ia "
const res = await fetch("http://127.0.0.1:8000/chat/holacomoestas")
console.log(prompt)
const datos =await res.json()

console.log(datos)
