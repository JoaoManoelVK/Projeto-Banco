export class Entity {
  id!: number;
  createdAt!: Date;
  updatedAt!: Date;

  toJSON() {
    return {
      id: this.id,
      createdAt: this.createdAt,
      updatedAt: this.updatedAt,
    };
  }
}
