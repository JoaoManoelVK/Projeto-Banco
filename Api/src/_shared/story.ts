export interface Story<Input, Output> {
  execute(input?: Input): Promise<Output | void>;
}
