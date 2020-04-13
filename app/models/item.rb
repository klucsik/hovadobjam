class Item < ApplicationRecord
    has_many :onames
    belongs_to :material
    has_one :container, through: :material
end
