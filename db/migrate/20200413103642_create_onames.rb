class CreateOnames < ActiveRecord::Migration[6.0]
  def change
    create_table :onames do |t|
      t.string :name
      t.references :item, null: false, foreign_key: true

      t.timestamps
    end
  end
end
