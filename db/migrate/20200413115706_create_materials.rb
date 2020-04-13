class CreateMaterials < ActiveRecord::Migration[6.0]
  def change
    create_table :materials do |t|
      t.string :name
      t.belongs_to :container, null: false, foreign_key: true

      t.timestamps
    end
  end
end
