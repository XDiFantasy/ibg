from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey ,FLOAT, Text
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Strategy(Model):
    __tablename__ = "strategy"

    id = Column(Integer, primary_key=True)
    intro = Column(Text(512))
    sg_id = Column(Integer, ForeignKey('attr_ch.id'))
    pg_id = Column(Integer, ForeignKey('attr_ch.id'))
    sf_id = Column(Integer, ForeignKey('attr_ch.id'))
    pf_id = Column(Integer, ForeignKey('attr_ch.id'))
    c_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_sg_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_pg_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_sf_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_pf_id = Column(Integer, ForeignKey('attr_ch.id'))
    v_c_id = Column(Integer, ForeignKey('attr_ch.id'))

    sg = relationship('AttrCh',foreign_keys=sg_id)
    sf = relationship('AttrCh',foreign_keys=sf_id)
    pg = relationship('AttrCh',foreign_keys=pg_id)
    pf = relationship('AttrCh',foreign_keys=pf_id)
    c = relationship('AttrCh',foreign_keys=c_id)
    v_sg = relationship('AttrCh',foreign_keys=v_sg_id)
    v_pg = relationship('AttrCh',foreign_keys=v_pg_id)
    v_sf = relationship('AttrCh',foreign_keys=v_sf_id)
    v_pf = relationship('AttrCh',foreign_keys=v_pf_id)
    v_c = relationship('AttrCh',foreign_keys=v_c_id)


    def __repr__(self):
        return "<Strategy %r>" % self.id


class AttrCh(Model):
    __tablename__ = 'attr_ch'
    id = Column(Integer, primary_key=True)

    comment = Column(String(50))
    order = Column(String(200),default='fg_pct - three_pt_pct - fta_pct - oreb_pct - dreb_pct - ast_pct - tov_pct - stl_pct - blk_pct - pf_pct')
    fg_pct = Column(FLOAT,default=0)
    three_pt_pct = Column(FLOAT,default=0)
    fta_pct = Column(FLOAT,default=0)
    oreb_pct = Column(FLOAT,default=0)
    dreb_pct = Column(FLOAT,default=0)
    ast_pct = Column(FLOAT,default=0)
    tov_pct = Column(FLOAT,default=0)
    stl_pct = Column(FLOAT,default=0)
    blk_pct = Column(FLOAT,default=0)
    pf_pct = Column(FLOAT,default=0)

    def __repr__(self):
        return '<AttrCh %r : %r>' % (self.id, self.comment)


class Equip(Model):
    __tablename__ = 'equip'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    attr_ch_id = Column(Integer, ForeignKey('attr_ch.id'))

    attr_ch = relationship('AttrCh')
    

    def __repr__(self):
        return "<Equip %r, %r, %r>" % (self.id, self.name, self.attr_ch_id)      
