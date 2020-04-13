class AddMaterialRefToItems < ActiveRecord::Migration[6.0]
  def change
    add_reference :items, :material, null: true, foreign_key: true
  end
end
