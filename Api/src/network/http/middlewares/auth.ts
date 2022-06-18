import { Funcionario } from "@/domain/funcionario/funcionario.entity";
import { AutenticarPessoaStory } from "@/domain/pessoa/stories/autenticar.story";
import { PessoaInMemoryRepository } from "@/persistence/in-memory/pessoa.repository";
import { NextFunction, Request, Response, Router } from "express";

export async function getAuthUser(
  req: Request,
  res: Response,
  next: NextFunction
) {
  const tokenBase64 = req.headers.authorization;

  if (!tokenBase64) {
    return res.status(401).json({ error: `Usuário não autenticado!` });
  }

  const pessoas = PessoaInMemoryRepository.get();

  const userId = Number(
    Buffer.from(tokenBase64, "base64").toString("utf-8").split(":").at(-1)
  );

  const pessoa = await pessoas.findById(userId);

  if (!pessoa) {
    return res.status(401).json({ error: `Usuário não autenticado!` });
  }

  req.pessoa = pessoa;

  next();
}

export function validarPermissoes(
  validator: (permissoes: Set<string>) => boolean
) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (
      !(
        req.pessoa &&
        req.pessoa instanceof Funcionario &&
        validator(req.pessoa.cargo.permissoes)
      )
    ) {
      return res.status(401).json({ error: `Usuário não autenticado!` });
    }

    next();
  };
}
