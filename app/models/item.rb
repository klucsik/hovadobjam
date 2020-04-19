class Item < ApplicationRecord
    has_many :onames, dependent: :destroy
    belongs_to :material
    has_one :container, through: :material
end
