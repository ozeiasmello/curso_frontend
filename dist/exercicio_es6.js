const alunos = [
    { nome: 'João', nota: 7.8 },
    { nome: 'Maria', nota: 5.6 },
    { nome: 'Pedro', nota: 8.5 },
    { nome: 'Ana', nota: 6.9 },
    { nome: 'Paulo', nota: 4.3 },
    { nome: 'Julia', nota: 9.2 }
];

const alunosAprovados = alunos.filter(aluno => aluno.nota >= 6);

console.log(alunosAprovados);
